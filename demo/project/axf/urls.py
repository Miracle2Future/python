from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    # url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    url(r'^market/$',views.market,name="market"),
    url(r'^cart/$', views.cart, name='cart'),

    #修改购物车
    url(r'^changecart/(\d+)/$',views.changecart,name='changecart'),
    url(r'^mine/$', views.mine, name='mine'),
    #登录
    url(r'^login/$',views.login,name='login'),
    #注册
    url(r'^register/$',views.register,name='register'),
    #验证
    url(r'^checkuserid/$',views.checkuserid,name='checkuserid'),
    #退出
    url(r'^quit/$',views.quit,name='quit'),
]