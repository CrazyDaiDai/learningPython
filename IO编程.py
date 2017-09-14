
#!/user/bin/env python3
# -*- coding: UTF-8 -*-

'IO 编程 IO 在计算机中指 Input/Output 也就是输入和输出  Stream(流)是一个很重要的概念'
"文本文件用 标识符'r',二进制文件用 标识符'rb',"

'文件读写'

# 读文件 使用内置的 open() 函数,传入文件名和标识符
# f = open('/Users/aishangsaisai/Desktop/hellow.py','r') #标识符 r 表示读
# fread = f.read()
# print(fread)
# f.close()

"由于文件读写都有可能产生IOError,一旦出错 close() 就会不执行 所以为了保证文件能正确关闭,可以使用 try..finally..来实现"
# try:
# 	f = open('/Users/aishangsaisai/Desktop/hellow.py','r')
# 	print(f.read())
# finally:
# 	if f:
# 		print("f.close()")
# 		f.close()
'每次都写 try..finally.. 实在太繁琐,python引用了 with 语句来帮我们调用close()'
# with open('/Users/aishangsaisai/Desktop/hellow.py','r') as f:
# 	print(f.read())

'调用 read() 会一次性读取文件全部内容,文件很大的时候内存就会爆炸'
'可以贩毒调用 read(size) 方法,每次最多读取 size 个字节的内容'
'调用 readline() 可以每次读取一行内容,调用 readlines() 一次读取所有内容并按行返回 list'
'所以,当文件很小的时候一次性读取最方便 read(),不确定文件大小反复调用 read(size) 最保险,配置文件调用 readlines() 最方便'

# with open('/Users/aishangsaisai/Desktop/hellow.py','r') as f:
# 	for line in f.readlines():
# 		# print(line)
# 		print(line.strip()) # 去除末尾的'\n'

'file-like Object'
# with open('/Users/aishangsaisai/Desktop/照片/0b55b319ebc4b7456c8d4c8ecffc1e178a821508.jpg','rb') as f:
# 	print(f.read()) # 16进制表示的字符串


# 写入文件
# with open('/Users/aishangsaisai/Desktop/hellow.py','w') as f:
# 	f.write("print('hellow,world')")


#  StringIO 和 BytesIO

'很多时候数据的读取不一定是文件,也可以在内存中读写.StringIO顾名思义就是在内存中读写str'
from io import StringIO
# f = StringIO()
# f.write('Hellow')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())  #  getvalue() 用于获取写入后的str
#  读取StringIO
# f = StringIO('Hellow!\nHi!\nGoodbye!')
# while True:
# 	s = f.readline()
# 	if s == '':
# 		break
# 	print(s.strip())

'BytesIO 如果需要操作二进制数据,就需要使用BytesIO 跟上边rb,wb类似'
from io import BytesIO
# f = BytesIO()
# f.write('中国'.encode('utf-8'))
# print(f.getvalue())

# # f = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
# f = BytesIO('人闲桂花落,夜静春山空'.encode('utf-8'))
# print(f.read())

# 操作文件和目录

import os
# print(os.name) # 操作系统类型
# print(os.uname()) # 获取详细的系统信息
# print(os.environ)  # 环境变量

'操作文件和目录,查看,创建,删除'
# # 查看当前目录的绝对路径
# print(os.path.abspath('.'))
# # 在某个目录下创建一个新的目录,首先把新目录的完整路径表示出来
# path = os.path.join(os.path.abspath('.'),'textdir')
# print(path)
# # 然后创建一个目录 创建之后才会显示到文件当中
# os.mkdir(path)
# # 删除目录
# os.rmdir(path

'把两个路径合成成一个时,不要直接拼接字符串,而是通过 os.path.join() 函数 这样可以正确处理不同操作系统的路径分隔符'
'同样的道理,要拆分时 通过 os.path.split() 函数,后面一部分总是最后级别的目录或文件名'

# path = os.path.abspath('.')
# split = os.path.split(path)
# print(split)

# path = os.path.abspath('.')
# joinPath = os.path.join(path,"test.txt")
# # os.mkdir(joinPath)
# splitPath = os.path.split(joinPath)
# print(splitPath)
# '获取文件扩展名 os.path.splitext()'
# splitext = os.path.splitext(joinPath)
# print(splitext)

# '重命名文件'
# # os.rename('test.text','test.py')
# '删除文件'
# os.remove('test.py')


'序列化'
# 我们把变量从内存中编程可存储或传输的过程称之为序列化 在 python 中叫 pickling
# 反过来,把变量内容从序列化的对象重新读到内存里称之为反序列化 即 unpickling
'python 提供了 pickle 模块来实现序列化'

import pickle

# # 序列化
# d = dict(name = 'Bob',age = 18,score = 99)
# print(pickle.dumps(d))

'pickle.dumps() 方法把任意对象序列化成一个 bytes ,然后把这个bytes 写入文件'
'或者用赢一个方法 pickle.dump() 直接把对象序列化写入一个 file-like Object'

# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

# 反序列化
'pickle.loads()  pickle.load()'
# f = open('dump.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)
'不同版本的python中的pickle可能是不同的,因此 只能用pickle保存一些不重要的数据,不能成功反序列化也没关系'

# JSON
'内置的 json 模块'

import json

# d = dict(name = 'Bob',age = 18,score = 99)
# j = json.dumps(d)
# print(j)
# # 存
# f = open('JSON.txt','w')
# j = json.dump(d,f)
# f.close()
# # 取
# f = open('JSON.txt','r')
# j = json.load(f)
# f.close()
# print(j)

'JSON 进阶'
# python 的 dict 对象可以直接序列化为 JSON 的 {} ,不过很多时候,我们更喜欢用 class 表示对象,比如 Student 然后序列化

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob',18,99)
# print(json.dumps(s))
def student_dict(stu):
	return {
		'name' : stu.name,
		'age' : stu.age,
		'score' : stu.score
	}
# 存
f = open('JSON.txt','w')
json.dump(student_dict(s),f,default=student_dict)
f.close()
#取
f = open('JSON.txt','r')
j = json.load(f)
f.close()
print(j)