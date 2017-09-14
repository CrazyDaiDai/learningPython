#
# 面向对象高级编程
#

#  使用 __slots__

# class Student(object):
# 	pass
# 	# def set_score(self,score):
# 	# 	self.score = score

# s = Student()
# s.name = "zhangsan" # 动态给实例绑定一个属性
# print(s.name)
# # Student.name = "wangwu"
# # print(Student.name)

# # s.set_score(100)
# # print(s.score)

# def set_age(self,age):
# 	self.age = age

# Student.set_age = set_age # 给class绑定一个方法,对每一个实例都会起作用

# s.set_age(18)
# print("forever%s" % s.age)

# s2 = Student()
# s2.set_age(25)
# print(s2.age)

# 
#  如果我们想要限制实例的属性 值允许实例添加 name和score属性 定义一个特殊的 __slots__ 变量来限制
# 

# class Student(object):
# 	__slots__ = ("name","score")

# s = Student()
# s.name = "Kimi"
# s.score = 80
# # s.age = 18 # 'Student' object has no attribute 'age' 
# # 使用 __slots__ 定义的属性只对当前类实例起作用,对集成的子类不起作用

# class GraduateStudent(Student):
# 	__slots__ = ("age") # 除非子类也定义了 __slots__,这样子类实例允许定义的属性是自身的__slots__加上父类的__slots__
# 	# pass

# g = GraduateStudent()
# g.age = 18
# g.score = 99
# print(g.age,g.score)

# 
#  #property 
# 

# class Student(object):

# 	def get_score(self):
# 		return self.score

# 	def set_score(self,score):
# 		if not isinstance(score,int):
# 			raise ScoreError("score must be an integer")
# 		if 0 > score or score > 100:
# 			raise ScoreError("score must between 0 ~ 100")
# 		self.score = score
# s = Student()
# # s.set_score(1001)
# # s.set_score("123")
# s.set_score(99)
# print(s.score)

# class Student(object):

# 	@property
# 	def score(self):
# 		return self._score

# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ScoreError("score must be an integer")
# 		if 0 > value or value > 100:
# 			raise ScoreError("score must between 0 ~ 100")
# 		self._score = value

# s = Student()
# s.score = 100
# print(s.score)

#  巩固一把 巩固一把 巩固一把

# class Student(object):

# 	@property
# 	def score(self):
# 		return self._score

# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError("score must be an integer")
# 		if 0 > value or value > 100:
# 			raise ValueError("score must between 0 ~ 100")
# 		self._score = value

# s = Student()
# s.score = 99
# print(s.score)
# # s.score = "abc"
# # s.score = 101

#  练习
#  请利用@property给一个Screen对象加上width和height属性,以及一个只读属性resolution

# class Screen(object):

# 	@property
# 	def width(self):
# 		return self._width
# 	@width.setter
# 	def width(self,value):
# 		self._width = value

# 	@property
# 	def height(self):
# 		return self._height
# 	@height.setter
# 	def height(self,value):
# 		self._height = value

# 	@property
# 	def resolution(self):
# 		return self._width * self._height

# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)

# 
#  定制类
# 

# class Student(object):
# 	def __init__(self,name):
# 		self.name = name
# 	def __str__(self):
# 		return "Student object (name :%s)" % self.name
# 	__repr__ = __str__   

# print(Student("Tom"))
# s = Student("Kimi")
# print(s)

#  __iter__

# class Fib(object):

# 	def __init__(self):
# 		self.a,self.b = 0,1
	
# 	def __iter__(self):
# 		return self # 实例本身就是迭代器,所以返回自己

# 	def __next__(self):
# 		self.a,self.b = self.b,self.a + self.b
# 		if self.a > 1000:
# 			raise StopIteration() #__next__() 方法是拿到循环的下一个值,直到遇见 StopIteration() 时退出循环
# 		return self.a

# 	def __getitem__(self,n):
# 		self.a,self.b = 0,1
# 		for x in range(n + 1):
# 			self.a,self.b = self.b,self.a + self.b
# 		return self.a

# for n in Fib():
# 	print(n)

# '虽然Fib可以作用与for循环,看起来有点类似 list 但是把它直接当做list使用还是不行的'
# # print(Fib()[5]) # 'Fib' object does not support indexing

# '要想像 list 那样根据下标来取值 需要实现 __getitem__() 方法'
# print(Fib().__getitem__(4))

#  __getattr__

# class Student(object):
	
# 	def __init__(self):
# 		self.name = "Tom"

# print(Student().name) # 调用 name 属性没有问题
# print(Student().score) # 但是调用没有的 score 属性就会出现问题
# '要避免这个错误,除了可以加上一个 score 属性外,python 还有另外一种机制,就是写一个 __getattr__方法 动态返回一个属性'
# class Student(object):

# 	def __init__(self):
# 		self.name = "Tom"

# # 	def __getattr__(self,attr):
# # # '当调用不存在的属性时,解释器会试图调用 __getattr__(self,'score') 来尝试获得属性'
# # 		if attr == "score":
# # 			return 99
# 	'也可以返回一个函数'
# 	def __getattr__(self,score):
# 		if score == "score":
# 			return lambda: 25
# 	# '当定义了 __getattr__ 之后调用没有的属性默认返回 None '
# 	# '要让类只响应特定的几个属性 我们就要按照约定,抛出 AttributeError 的错误'
# 		raise AttributeError('\'Student\' object has no attribute \'%s\'' % score)

# # print(Student().name)
# # print(Student().score)

# print(Student().name) # 返回函数的写法
# score = Student().score
# print(score())
# print(Student().age) 


# __call__  定义 __call__ 方法,就可以直接对实例进行调用 
# class Student(object):
	
# 	def __init__(self,name):
# 		self.name = name
# 	def __call__(self):
# 		print("My name is %s" % self.name)

# s = Student('Tom')
# s()
# Student('Kimi')()
# #  Callable
# '通过 callable() 函数,可以判断一个对象是否是"可调用"对象 返回一个bool值-> False or True'
# print(callable(s))
# print(callable([1,2,3]))



# 
#  使用枚举
# 

# 'enum'

# from enum import Enum

# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

# for name,member in Month.__members__.items():
# 	print(name,'=>',member,',',member.value)

# '如果想要更精准的控制枚举类型,可以从 Enum 派生出自定义类'
# from enum import Enum,unique
# '@unique 装饰器可以帮助我们检查 保证没有重复值'
# @unique   
# class Weekday(Enum):
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thu = 4
# 	Fri = 5
# 	Sat = 6

# '访问这些枚举'
# day1 = Weekday.Mon
# print(day1)
# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(Weekday(3))


# 
#  使用元类
# 

from 模块 import Hellow

h = Hellow()
# print(dir(h))
h.hellow('dandan')
# print(type(h))






