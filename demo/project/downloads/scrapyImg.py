#-*- coding:utf-8 -*-
#__author__:"Owen Zhao"

'''

获取url项目图片

'''

import urllib.request
import os,time

type_list = [
    'axf_wheel',
    'axf_nav',
    'axf_mustbuy',
    'axf_shop',
    'axf_goods',
]

def getImgUrl():
    with open('img_url.data','r') as f:
        data = f.readlines()
        # url = data[0].split(',')[0].split('(')[1].split('\"')[1]
        # print(data[0].split(',')[0].split('(')[1].split('\"')[1])

        num = 1
        name_type = ''
        for i in range(len(data)):
            # print(data[i].split(",")[0].split("(")[1].split('\"')[1])
            url = data[i].split(",")[0].split("(")[1].split('\"')[1]
            if num<6:
                name_type = type_list[0]
            elif num<10:
                name_type = type_list[1]
            elif num<14:
                name_type = type_list[2]
            elif num<25:
                name_type = type_list[3]
            else:
                name_type = type_list[4]
            saveImg(url,num,name_type)
            num += 1
    getImgUrlGoods()


def getImgUrlGoods():
    with open('axf_goods.data','r') as f:
        data = f.readlines()
        num = 1
        start_time = time.time()
        for i in range(len(data)):
            url = data[i].split('values("')[1].split('"')[2]
            # print(url)
            name_type = type_list[4]
            saveImg(url,num,name_type)
            num += 1
        end_time = time.time()
        spend_time = end_time - start_time
        print(spend_time)

def saveImg(url,num,name_type):
    # print(url)
    # url = "http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg"
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 下载的图片存放地址
    # print(base_dir)
    saveDir = base_dir + '/imgs'
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    savePath = saveDir+'/{}_00{}'.format(name_type,str(num)) +'.jpg'
    # if not savePath:
    # print('savePath')
    urllib.request.urlretrieve(url,savePath)    #将图片地址url保存到本地


if __name__ == '__main__':
    getImgUrlGoods()

'''
axf_wheel
("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg","酸奶女王","21870"),
("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),
("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),
("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),
("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");

axf_nav
("http://img01.bqstatic.com//upload/activity/2017032016495169.png","每日必抢","21851"),
("http://img01.bqstatic.com//upload/activity/2016121920130294.png","每日签到","21753"),
("http://img01.bqstatic.com//upload/activity/2017010517013925.png","鲜货直供","21749"),
("http://img01.bqstatic.com//upload/activity/2017031518404137.png","鲜蜂力荐","21854");

axf_mustbuy
("http://img01.bqstatic.com//upload/activity/2017031715194326.jpg@90Q.jpg","酸奶女王","21870"),
("http://img01.bqstatic.com//upload/activity/cms_118826_1489742316.jpg@90Q","鲜果女王","21861"),
("http://img01.bqstatic.com//upload/activity/2017031011044918.jpg@90Q.jpg","麻辣女王","21866"),
("http://img01.bqstatic.com//upload/activity/2017022318314545.jpg@90Q.jpg","鲜货直供－果析","21858");

axf_shop
("http://img01.bqstatic.com//upload/activity/2016121616565087.png@90Q.png","闪送超市","1464"),
("http://img01.bqstatic.com//upload/activity/2017031018405396.png@90Q.png","热销榜","104749"),
("http://img01.bqstatic.com//upload/activity/2017031018403438.png@90Q.png","新品尝鲜","104747"),
("http://img01.bqstatic.com//upload/activity/2016121618424334.png@90Q.png","牛奶面包","103536"),
("http://img01.bqstatic.com//upload/activity/2016121617150246.png@90Q.png","饮料酒水","103549"),
("http://img01.bqstatic.com//upload/activity/201612161714501.png@90Q.png","优选水果","103532"),
("http://img01.bqstatic.com//upload/activity/2016121618550639.png@90Q.png","更多","100001"),
("http://img01.bqstatic.com//upload/activity/2017031318520359.jpg@90Q.jpg","鲜蜂力荐","21854"),
("http://img01.bqstatic.com//upload/activity/2016121618233839.png@90Q.png","卤味-鸭货不能停","21742"),
("http://img01.bqstatic.com//upload/activity/2016121618232773.png@90Q.png","零食轰趴","21142"),
("http://img01.bqstatic.com//upload/activity/2016121618235123.png@90Q.png","整箱购","20581");

'''