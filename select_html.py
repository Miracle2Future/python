# IO多路复用

# epoll并不代表一定比select好
# 在并发高的情况下,链接活跃度不是很高   epoll比select 好    例如:网站
# 并发不高的情况下,连接活跃度高         select比epoll 好    例如:游戏实时数据访问

## 非阻塞IO实现http请求


import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from urllib.parse import urlparse

# 使用select完成http请求
# 爬取网站源码

selector = DefaultSelector()
urls = ["https://www.baidu.com"]
stop = False


class Fetcher:

    def connected(self, key):
        selector.unregister(key.fd)
        msg = "GET {} HTTP/1.1\r\nHost{}\r\nConnection:close\r\n".format(self.path, self.host).encode("utf8")
        self.client.send(msg)
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            with open('{}.html'.format(self.host), 'wb') as f:
                f.write(self.data)
            print('download success end')
            self.client.close()
            urls.remove(self.spider_url)
            print(urls)
            print(stop)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        print(url)
        self.host = url.netloc
        
        self.path = url.path
        self.data = b""
        print("host:{}, path:{}".format(self.host,self.path))
        if self.path == '':
            self.path = "/"
        
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

def loop():
    # 事件循环,不停地请求socket的状态并调用对应的回调函数
    #1 select本事不支持register模式
    #2 socket状态变化以后的问题室友程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 回调 + 事件循环 + selector(select/epool) linux默认使用epool


fetcher = Fetcher()
fetcher.get_url(urls[0])
loop()
