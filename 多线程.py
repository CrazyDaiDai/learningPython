
# 多线程

'python 提供了两个模块:_thread 和 threading,_thread是低级模块.threading是对_thread进行了封装的高级模块'

'启动一个线程就是把一个函数传入并创建 Thread 实例,然后调用 start() 开始执行'

# import time,threading,random
# # 新线程执行的代码
# def loop():
# 	print('thread %s is running...' % threading.current_thread().name)
# 	n = 0
# 	while n < 5:
# 		n = n + 1
# 		print('thread %s >>> %s' % (threading.current_thread().name,n))
# 		# time.sleep(random.random()) # 睡随机时间
# 		time.sleep(1) # 睡一秒
# 	print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target = loop,name = 'LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 这是一个错误的例子 看看没见线程锁 是怎么把内容改乱的吧
# import time,threading
# # 假装自己是存款
# balance = 0

# def change_it(n):
# 	# 先存后取
# 	global balance
# 	balance = balance + n
# 	balance = balance - n

# def run_thread(n):
# 	for i in range(100000):
# 		change_it(n)

# t1 = threading.Thread(target = run_thread,args = (5,))
# t2 = threading.Thread(target = run_thread,args = (8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 线程锁 lock

# import time,threading

# balance = 0
# lock = threading.Lock()

# def run_thread(n):
# 	for i in range(100000):
# 		# 先要获取锁
# 		lock.acquire()
# 		try:
# 			change_it(i)
# 		finally:
# 			# 改完之后一定要释放锁
# 			lock.release()

# def change_it(n):
# 	global balance
# 	balance = balance + n
# 	balance = balance - n

# t1 = threading.Thread(target = run_thread,args = (5,))
# t2 = threading.Thread(target = run_thread,args = (8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

'ThreadLocal'
'在多线程环境下,每个线程都有自己的数据,一个线程使用自己的局部变量比使用全局变量好,因为局部变量只有线程自己能看见,'
'不会影响其他线程,而全局变量的修改必须加锁'

# import threading
# #  创建全局 ThreadLocal对象
# local_school = threading.local()

# def procress_student():
# 	# 获取当前线程关联的student:
# 	std = local_school.student
# 	print('Hellow, %s (in %s)' % (std,threading.current_thread().name))


# def procress_thread(name):
# 	# 绑定ThreadLocal的student
# 	local_school.student = name
# 	procress_student()

# t1 = threading.Thread(target = procress_thread,args = ('Alice',),name = 'Thread-A')
# t2 = threading.Thread(target = procress_thread,args = ('Bob',),name = 'Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

'分布式进程'
# import random,time,queue
# from multiprocessing.managers import BaseManager

# # 发送任务的队列
# task_queue = queue.Queue()
# # 接受结果的队列
# result_queue = queue.Queue()

# # 从BaseManager集成的QueueManager
# class QueueManager(BaseManager):
# 	pass

# # 把两个Queue都注册到网络上,callable参数关联了Queue对象
# QueueManager.register('get_task_queue',callable = lambda : task_queue)
# QueueManager.register('get_result_queue',callable = lambda : result_queue)
# # 绑定端口5000,设置验证码'abc'
# manager = QueueManager(address = ('',5000),authkey = b'abc')
# # 启动Queue
# manager.start()
# # 获得通过网络访问的Queue对象
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去
# for i in range(10):
# 	n = random.randint(0,10000)
# 	print('Put task %d...' % n)
# 	task.put(n)
# # 从result队列读取结果
# print('Try get results...')
# for i in range(10):
# 	r = result.get(timeout = 10)
# 	print('Result : %s' % r)
# # 关闭
# manager.shutdown()
# print('master exit.')

'正则'
'''
1.创建一个匹配邮箱的正则表达式
2.用该正则表达式去匹配用户的输入来判断是否合法
用 \d 可以匹配一个数字, \w 可以匹配一个字母或数字
'00\d' 可以匹配 '007' 但无法匹配 '00A'
'\d\d\d' 可以匹配 '010'
'\w\w\d' 可以匹配 'py3'
. 可以匹配任意字符
'py.' 可以匹配 'pyc','py0','py!'
要匹配变长的字符串,在正在表达式中,
* 表示任意个字符(包括0个),
+ 表示至少一个字符,
? 表示0个或1个字符
用 {0} 表示 n 个字符,用 {n,m} 表示 n~m 个字符,
\s 可以匹配一个空格,用 \s+ 表示至少有一个空格 ' ','  '
'''
'正则进阶'
"""
要做更精确的匹配,可以用 [] 表示范围
[0-9a-zA-Z\_] 可以匹配一个数字或者字母或者下划线
[0-9a-zA-Z\_]+ 可以匹配至少由一个数字或者字母或者下划线组成的字符串,'a100','o_z','Py3000'
[a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母或下划线开头,后接任意个由数字或字母或者下划线组成的字符串,也就是python的合法变量
[a-zA-Z\_][0-9a-zA-Z\_]{0,19} 更精确的限制了变量的长度是1-20个字符(前边一个 后边最多19个)
A|B 可以匹配A或者B 所以 (P|p)ython 可以匹配 'Python' 或者 'python'
^ 表示行的开头 ^\d 表示必须以数字开头
$ 表示行的结尾 \d$ 表示必须以数字结束
"""
're模块'
import re
s = re.match(r'^\d{3}\-\d{3,8}$','010-1234')
print(s) # 匹配成功返回一个 match 对象 否则返回 None
'''
伪代码:
test = '用户的输入'
if re.match(r'正则表达式',test):
	print('成功')
else:
	print('失败')
'''

'正则切分字符串'
s = 'a b  c'
print(re.split(r'\s+',s))
print(re.split(r'[\s\,]+','a,b,c  d,e'))
print(re.split(r'[\s\,\;]+','a,b  c;d;;e'))

'分组'
'除了简单的判断是否匹配之外,正则表达式还有提取字符串的强大功能,用()表示的就是要提取的分组(Group)'
m = re.match(r'^(\d{3})-(\d{0,9})$','010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

'贪婪匹配'
'需要特别之处的是:正则匹配默认是贪婪匹配,也就是匹配尽可能多的字符'
print(re.match(r'^(\d+)(0*)$',"102300").groups())
'由于 \d+ 采用贪婪匹配,直接把后面的0全部匹配了,结果 0* 只能匹配到空字符串了'

'必须让 \d+ 采用非贪婪匹配(也就是尽可能少的匹配),才能吧后面的00匹配出来,加个 ? 就可以让 \d+ 采用非贪婪匹配'
print(re.match(r'^(\d+?)(0*)$',"102300").groups())

'编译'
'如果一个正则表达式要重复使用几千次,处于效率考虑,我们可以预编译该正则表达式,接下来重复使用时就不需要编译这个步骤了,直接匹配'
# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-10086').groups())
'编译后生成 Regular Expression 对象,由于该对象自己包含了正则表达式,所有调用对应的方法是不用给出正则字符串'

re_email = re.compile(r'^([0-9a-zA-Z\_\.]+?)\@([0-9a-zA-Z\_]+?.com)$')
print(re_email.match("szcls89@gmail.com"))
print(re_email.match("bill.gates@microsoft.com"))
# email = re.match(r'^([0-9a-zA-Z\_]+?)\@([0-9a-zA-Z\_]+?.com)$','szcls89@gmail.com')
# print(email)

