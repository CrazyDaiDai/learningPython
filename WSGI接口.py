'了解了HTTP协议和HTML文档,我们其实就明白了一个Web应用的本质就是:'
'''
1.浏览器发送一个HTTP请求
2.服务器接受请求,生成一个HTML文档
3.服务器把HTML文档作为HTTP响应的Body发送给服务器
4.浏览器收到HTTP响应,从HTTP Body取出HTML文档显示
'''
'WSGI : Web Server Gateway Interface'
'WSGI 接口定义非常简单,它只要求Web开发者实现一个函数,就可以响应HTTP请求'

# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type';'text/html')])
#     return [b'<h1>Hellow,web!</h1>']
'''
上面的application()函数就是符合WSGI标准的一个HTTP处理函数,它接收两个参数:
    environ:一个保险所有HTTP请求信息的dict对象;
    start_response: 一个发送HTTP响应的函数
在application()函数中,调用:
    start_response('200 OK',[('Content-Type','text/html')])
就发送了HTTP响应的Header,注意Header只能发送一次,也就是只能调用一次start-responce()函数,这个函数接收两个参数,
一个是HTTP响应码,一个是一组list表示HTTP Header,每个Header用一个包含两个str和tuple表示
然后,函数返回值 b'<h1>Hellow,web</h1>' 将作为HTTP响应的Body发送给浏览器
有了WSGI,我们关心的就是如何从environ这个dict对象拿到HTTP请求信息,然后构造HTML,通过start-response()发送header,最后返回Body.
application()函数必须由WSGI服务器来调用
'''
'Python内置了一个WSGI服务器,这个模块叫wsgiref,它的实现完全符合WSGI标准,但是不考虑任何运行效率,仅供开发和测试使用'


# hellow.py
# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type','text/html')])
#     return [b'<h1>Hellow,web!</h1>']

# localhost:8000

# server.py 负责启动WSGI服务器,加载application()函数

'如果你觉得这个Web应用太简单了,可以稍微改造一下,从environ里读取PATH_INFO,这样可以显示更加动态的内容'
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text.html')])
    body = b'<h1>Hellow,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
#  localhost:8000/Michael


