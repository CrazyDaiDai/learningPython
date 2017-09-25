'TCP编程'

'创建一个基于TCP链接的socket'
# # 导入 socket 库
# import socket
# # 创建一个socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 建立连接
# s.connect(('www.sina.com.cn',80))
#
# '创建 socket 时,AF_INET 指定使用 IPv4 协议,如果要用更先进的 IPv6,就指定 AF_INET6.'
# 'SOCK_STREAM 指定使用面向流的TCP协议,这样,一个 socket 对象就创建成功了,但是还没有建立连接'
# '客户端要主动发起TCP连接,必须知道服务器的IP地址和端口号,新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址,但是怎么知道新浪服务器的端口号呢?'
# '答案是作为服务器,提供什么样的服务,端口号就必须固定下来,由于我们想要访问网页,因此新浪提供网页服务的服务器必须吧端口号固定在80段口'
# '因为80端口是Web服务的标准端口,其他服务都有对应的标准端口号,例如 SMTP服务是25端口,FTP服务是21端口.'
# '端口号小于1024的是Internet标准服务的端口,端口号大于1024的,可以任意使用'
#
# '因此,我们链接新浪服务器的代码如下'
# # s.connect(('www.sina.com.cn',80))
# '注意参数是一个 tuple,包含地址和端口号'
# '建立TCP连接后,我们就可以向新浪服务器发送请求,要求返回首页的内容'
# # 发送数据,请求首页的内容
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     # 每次最多接收1k字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# '接收数据时,调用 recv(max) 方法,一次最多接收指定的字节数,因此,在一个while循环中反复接收,直到 recv() 返回空数据,表示接收完毕'
# '当我们接受完数据后,调用 close() 方法关闭 socket,这样,一次完整的网络通信就结束了'
# # 关闭连接
# s.close()
# '接收到的数据包括HTTP头和网页本身,我们只需要把HTTP头和网页分离一下,把HTTP头打印出来,网页内容保存到文件'
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('sina.html','wb') as f:
#     f.write(html)

'服务器'
'服务器进程首先要绑定一个端口并监听来自其他客户端的连接,如果客户端连接过来了,服务器就与客户端建立socket连接,随后的通信就靠这个socket连接了'
'所以,服务器打开固定端口(比如80)监听,每来一个客户端连接,就创建socket连接,由于服务器会有大量来着客户端的连接'
'所以,服务器要能够区分一个socket连接是和哪个客户端绑定的.'
'一个socket依赖4项:服务器地址,服务器端口,客户端地址,客户端端口.来唯一确定一个socket'
'但是服务器还需要同时响应多个客户端的请求,所以每个连接都需要一个新的进程或者新的线程来处理,否则服务器一次就只能服务一个客户端.'

'一个简单的案例↓'
import socket
import threading
import time

def tcplink(sock,addr):
    print('接受新的连接 %s:%s...' % addr)
    sock.send(b'Welcom!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hellow,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('连接 %s:%s 关闭' % addr)

# 创建一个基于 IPv4和TCP协议的socket:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定IP和指定端口号 127.0.0.1 是一个特殊的IP地址,它绑定的是本机地址
s.bind(('127.0.0.1',9999))
# 调用 listen() 方法开始监听端口,传入的参数指定等待连接的最大数
s.listen(5)
print('等待连接中...')
# 接下来,服务器程序通过一个永久循环来接受来自客户端的连接,accept() 会等待并返回一个客户端的连接:
while True:
    # 接受一个新的连接
    sock,addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target = tcplink,args = (sock,addr))
    t.start()
