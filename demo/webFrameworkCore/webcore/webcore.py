#-*-coding:utf-8-*-
#- python version:3.0+
'''
    web framework core code

'''
from wsgiref.simple_server import make_server
from Controller import admin

#处理url
URL_DICT = {
    "/":admin.handle_index,
    "/index":admin.handle_index,
    "/date":admin.handle_date
}

def RunServer(environ,start_response):
    '''
    :param environ:         客户发来的所有数据
    :param start_response:  封装要返回给用户的数据，响应头状态
    :return:                返回内容
    '''
    start_response('200 OK',[('Content-Type','text/html')])
    current_url = environ['PATH_INFO']
    print(current_url)
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
        if func:
            return func()
    else:
        return(['<h1>404</h1>'.encode('utf-8'),])

if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8000,RunServer)
    print('Server HTTP on PORT 8000')
    httpd.serve_forever()