'urllib'
'urllib 提供了一系列用于操作 URL 的功能'
'urllib 的 request 模块可以非常方便的抓取 URL 的内容,也就是发送一个 GET 请求到指定的界面,然后返回 HTTP 的响应'

from urllib import request

with request.urlopen('https://github.com/CrazyDaiDai') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('k --> %s : v --> %s' % (k,v))
    print('Data:',data.decode('utf-8'))

