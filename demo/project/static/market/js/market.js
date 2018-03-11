$(document).ready(function(){
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbtn = document.getElementById("showsortbtn")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"


    alltypebtn.addEventListener("click", function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)
    showsortbtn.addEventListener("click", function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click", function(){
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click", function(){
        sortdiv.style.display = "none"
    },false)


    //修改购物车
    // var addShoppings = document.getElementsByClassName("addShopping")
    // var subShoppings = document.getElementsByClassName("subShopping")
    //
    // //添加购物车
    // for (var i = 0; i < addShoppings.length; i++){
    //     addShopping = addShoppings[i]
    //     addShopping.addEventListener("click",function(){
    //         pid = this.getAttribute("ga")
    //         console.log("测试market.js")
    //         //向服务器发起AJAX请求
    //         $.post("changecart/0/",{"productid":pid},function(data){
    //             console.log("接受服务器数据")
    //             if (data.status == "success"){
    //                 //添加成功，把中间的span的innerHTML变成当前的数量
    //                 document.getElementById(pid).innerHTML = data.data
    //                 console.log("返回data:",data.data)
    //             }else{
    //                 console.log(" not login data:",data.data)
    //                 if (data.data == -1){
    //                     //  -1 表示当前操作没有用户登录
    //                     window.location.href = "http://127.0.0.1:8000/login/"
    //                 }
    //             }
    //         })
    //     })
    // //     console.log("addShoppings i",i)
    // }


    //修改购物车
    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")

    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]
        addShopping.addEventListener("click", function(){
            pid = this.getAttribute("ga")
            // alert("添加")
            $.post("/changecart/0/",{"productid":pid}, function(data){
                console.log(data)
                if (data.status == "success"){
                    console.log(data.status)
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                } else {

                    if (data.data == -1){
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        })
    }

    for (var i = 0;i < subShoppings.length;i++){
        subShopping = subShoppings[i]
        subShopping.addEventListener("click", function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/1/",{"productid":pid,},function(data){
                if (data.status == "success"){
                    document.getElementById(pid).innerHTML = data.data
                }else{
                    if (data.data == -1){
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        })
    }
    //
    // for (var i = 0; i < subShoppings.length; i++){
    //     subShopping = subShoppings[i]
    //     subShopping.addEventListener("click", function(){
    //         pid = this.getAttribute("ga")
    //         $.post("/changecart/1/",{"productid":pid}, function(data){
    //             if (data.status == "success"){
    //                 //添加成功，把中间的span的innerHTML变成当前的数量
    //                 document.getElementById(pid).innerHTML = data.data
    //             } else {
    //                 if (data.data == -1){
    //                     window.location.href = "http://127.0.0.1:8001/login/"
    //                 }
    //             }
    //         })
    //     })
    // }

})