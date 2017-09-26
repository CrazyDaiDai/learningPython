'''
def application(environ,start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ,start_response)
    if method == 'POST' and path == '/signin':
        return handle_signin(environ,start_response)
    ...
'''
'这样写下去代码肯定是无法维护了'

'选择一个比较流行的Web框架--Flask来使用'

from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_from():
    return '''<from action = "/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </from>'''

@app.route('/signin',methods=['POST'])
def signin():
    # 需要从request对象读取表单对象
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

'''
除了Flask,常见的Python Web框架还有:
Django 全能型Web框架
web.py 一个小巧的Web框架
Bottle 和Flask类似的Web框架
Tornado Facebook的开源异步Web框架
'''
