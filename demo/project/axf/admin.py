from django.contrib import admin
from .models import *

# Register your models here.

class WheelAdmin(admin.ModelAdmin):
    list_display = ('id','name','img','trackid')

class NavAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'trackid')

class MustbuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'trackid')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'trackid')

class MainShowAdmin(admin.ModelAdmin):
    list_display = ('id','trackid','name','categoryid','brandname')

class FoodTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'typeid', 'typename', 'typesort', 'childtypenames')

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','productid','productlongname','productnum','storenums')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','userAccount','userPasswd','userName','userPhone','userAddress','userImg','userRank','userToken')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','userAccount','productid','productname','productnum','productprice')

admin.site.register(Wheel,WheelAdmin)
admin.site.register(Nav,NavAdmin)
admin.site.register(Mustbuy,MustbuyAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(MainShow,MainShowAdmin)
admin.site.register(FoodTypes,FoodTypesAdmin)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Cart,CartAdmin)