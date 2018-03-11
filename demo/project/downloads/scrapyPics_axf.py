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


        num = 1
        for i in range(len(data)):
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
            name_type = type_list[4]
            saveImg(url,num,name_type)
            num += 1
        end_time = time.time()
        spend_time = end_time - start_time
        print(spend_time)

def saveImg(url,num,name_type):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 下载的图片存放地址
    saveDir = base_dir + '/imgs'
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    savePath = saveDir+'/{}_00{}'.format(name_type,str(num)) +'.jpg'
    urllib.request.urlretrieve(url,savePath)    #将图片地址url保存到本地


if __name__ == '__main__':
    getImgUrl()

