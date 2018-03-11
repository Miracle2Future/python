#-*-coding:utf-8-*-
import time

#处理函数
def handle_index():
    with open('Templates/index.html',mode='rb') as f:
        data = f.read()
        data = data.replace(b'@zxlovewxx','赵旭最爱王欣欣'.encode('utf-8'))
        data = data.replace(b'@time',str(time.time()).encode('utf-8'))
    return ([data, ])

def handle_date():
    return (['<h1>Hello, Web date</h1>'.encode('utf-8'), ])

