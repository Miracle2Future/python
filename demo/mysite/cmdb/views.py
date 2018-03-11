from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>CMDB</h1>')

def login(request):
    '''

    :param request: 请求的所有数据
    :return:
    '''
    #包含用户提交的所有信息
    # print(request.method)
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username == 'root' and password == '123456':
            print("success")
        else:
            error_msg = '用户名或者密码出错'
    return render(request,'login.html',{'error_msg':error_msg})


    # return HttpResponse('login')
