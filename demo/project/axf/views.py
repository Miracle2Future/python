from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from .forms.login import LoginForm
import time,random,os
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.

def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]

    mainList = MainShow.objects.all()
    return render(request,'axf/home.html',
                  {
                      'title':'主页',
                      'wheelsList':wheelsList,
                      'navList':navList,
                      'mustbuyList':mustbuyList,
                      'shop1':shop1,
                      'shop2':shop2,
                      'shop3':shop3,
                      'shop4':shop4,
                      'mainList':mainList,
                  })

def market(request):
    leftSlider = FoodTypes.objects.all()
    productList = Goods.objects.all()

    token = request.session.get("token")
    cartlist = []
    if token:
        user = User.objects.get(userToken=token)
        cartlist = Cart.objects.filter(userAccount=user.userAccount)
    for p in productList:
        for c in cartlist:
            if c.productid == p.productid:
                #将购物车商品数量传给p.num
                p.num = c.productnum
                continue
    return render(request,'axf/market.html',{
        'title':'闪送超市',
        'leftSlider':leftSlider,
        'productList':productList,
    })

def cart(request):
    '''
    购物车
    :param request:
    :return:
    '''
    cartslist = []
    token = request.session.get("token")
    if token != None:
        user = User.objects.get(userToken=token)
        cartslist = Cart.objects.filter(userAccount = user.userAccount)
    return render(request,'axf/cart.html',{'title':'购物车','cartslist':cartslist})


def changecart(request,flag):
    '''
    修改购物车
    :param request:
    :param flag:
    :return:
    '''
    #判断用户是否登录
    token = request.session.get("token")
    print(token)
    if token == None:
        #没有登录
        print("当前没有用户登录")
        return JsonResponse({"data":-1,"status":"error"})
    productid = request.POST.get("productid")
    product = Goods.objects.get(productid=productid)
    user = User.objects.get(userToken=token)

    if flag == '0':
        # 0代表往购物车添加商品
        #如果商品库存为0
        if product.storenums == 0:
            return JsonResponse({"data":-2,"status":"error"})

        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            #购物车是空的  直接增加一条订单
            c = Cart.createcart(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
            c.save()
        else:
            try:
                c = carts.get(productid = productid)
                #修改数量价格
                c.productnum += 1
                c.productprice = "%.2f"%(float(product.price)* c.productnum)
                c.save()
            except Cart.DoesNotExist as e:
                #直接添加一条订单
                c = Cart.createcart(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
                c.save()
        #库存减一
        product.storenums -= 1
        product.save()
        return JsonResponse({"data":c.productnum,"price":c.productprice,"status":"success"})
    elif flag == '1':
        # 1 代表从购物车去除商品
        carts = Cart.objects.filter(userAccount = user.userAccount)
        c = None
        if carts.count() == 0:
            return JsonResponse({"data":-2,"status":"error"})
        else:
            try:
                c = carts.get(productid = productid)
                #修改数量与价格
                c.productnum -= 1
                c.productprice = "%.2f"%(float(product.price) * c.productnum)
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()
            except Cart.DoesNotExist as e:
                return JsonResponse({"data":-2,"status":"error"})
        product.storenums += 1
        product.save()
        return JsonResponse({"data":c.productnum,"price":c.productprice,"status":"success"})
    elif flag == '2':
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid = productid)
        c.isChose = not c.isChose
        c.save()
        str = ''
        if c.isChose:
            str = '√'
        return JsonResponse({"data":str,"status":"success"})
    elif flag == '3':
        pass


def mine(request):
    '''

    :param request:
    :return:
    '''
    #读取session
    username = request.session.get("username","未登录")
    return render(request,'axf/mine.html',{'title':'我的','username':username})

def login(request):
    '''
    登录
    :param request:
    :return:
    '''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #信息格式没问题，验证账户密码的正确性
            # print("验证用户和密码")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print('username = {},password = {}'.format(username,password))
            try:
                user = User.objects.get(userAccount= username)
                if user.userPasswd != password:
                    return redirect("/login/")
            except User.DoesNotExist as e:
                return redirect("/login/")
            #登录成功
            token = time.time() + random.randrange(1,10000)
            user.userToken = str(token)
            user.save()
            request.session["username"] = user.userName
            request.session["userImg"] = user.userImg
            request.session["token"] = user.userToken
            return redirect('/mine/')
        else:
            return render(request,'axf/login.html',{"title":"登录","form":form,"error":form.errors})
    else:
        form = LoginForm();
        return render(request,'axf/login.html',{'title':'登录','form':form})

def register(request):
    '''
    注册
    :param request:
    :return:
    '''
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPassword = request.POST.get("userPass")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userAddress")
        userRank = 0
        token = time.time() + random.randrange(1,10000)
        userToken = str(token)
        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MDEIA_ROOT, userAccount + ".png")
        with open(userImg,"wb") as fp:
            for data in f.chunks(): #chunks 处理图片
                fp.write(data)

        user = User.createuser(userAccount,userPassword,userName,userPhone,userAddress,userImg,userRank,userToken)
        user.save()

        #设置session
        request.session["username"] = userName
        request.session["token"] = userToken


        return redirect('/mine/')
    return render(request,'axf/register.html',{'title':'注册'})

def checkuserid(request):
    '''
    注册用户时检测该用户是否已注册
    :param request:
    :return:
    '''
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount=userid)
        return JsonResponse({"data":"该用户已经被注册","status":"error"})
    except user.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})

def quit(request):
    logout(request)
    return redirect('/mine/')