#!/user/bin/env python3
#_*_ coding: utf-8 _*_

#
# 面向对象编程 Object Oriented Programming 简称OOP
#

# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name,score):
# 		super(Student, self).__init__()
# 		self.name = name
# 		self.score = score

# 	def print_score(self):
# 		print("name :%s,score :%s" % (self.name,self.score))

# std1 = Student("zhangsan",80)
# stu2 = Student("wangwu",90)
# std1.print_score()
# stu2.print_score()

#
# 类(class)和实例(Instance)
#		
# class Student(object):
# 	def __init__(self,name,score):
# 		super(Student,self).__init__()
# 		self.name = name
# 		self.score = score

# 	def print_score(self):
# 		print("name :%s,score :%s" % (self.name,self.score))

# 	def get_grade(self):
# 		if self.score >= 90:
# 			print("S")
# 		elif 70 <= self.score < 90:
# 			print("A")
# 		else:
# 			print("B")

# zhangsan = Student("zhangsan",90)
# zhangsan.print_score()
# zhangsan.get_grade()
# wangwu = Student("wangwu",66)
# wangwu.print_score()
# wangwu.get_grade()

# 
#  访问限制 变量以__开头的表示它是一个私有(private)变量 只能内部访问
# 

# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name, score):
# 		super(Student, self).__init__()
# 		self.__name = name
# 		self.__score = score

# 	def print_name_score(self):
# 		print("name :",self.__name,"score :",self.__score)
# 	def get_name(self):
# 		return self.__name
# 	def set_name(self,name):
# 		self.__name = name

# stu_1 = Student("zhangsan",90)
# stu_1.print_name_score()
# # stu_1.name = "lisi"
# '使用get,set可以在里边做一些类型或者逻辑的判断'
# stu_1.set_name("wangwu")
# stu_1.print_name_score()
# # 使用__开头的变量 其实也是可以在外部直接访问的,只是在python解释器中
# # 把__name变成了_Student__name
# stu_1._Student__name = "zhouxingxing" # 强烈建议不这么干,不同版本的解释器会把__name改成不同的变量名
# stu_1.print_name_score()

# isinstance(stu_1,Student)  #判断变量是否是某个类型可以用 isinstance() 来判断

# 
# 继承和多态
# 

# class Animal(object):
# 	def run(self):
# 		print("Animal running...")

# class Dog(Animal):
# 	def run(self):
# 		print("Dog running...")

# class Cat(Animal):
# 	def run(self):
# 		print("Cat running...")

# def run_twice(animal):
# 	animal.run()
# 	animal.run()

# Dog().run()
# Cat().run()
# Animal().run()

# run_twice(Dog())
		
# print(isinstance(Dog(),Animal))
# print(isinstance(Dog(),Cat))

# 
#  获取对象信息
# 
# import types

# # print(type("ABC") == str)
# # print(type("ABC") == type('abc'))
# # print(type(lambda x:x * x) == types.LambdaType)

# print(dir("ABC")) # 获取一个对象的所有属性和方法,可以使用 dir() 函数 对新手来说还挺有用的个人觉得
# print("ABC".title()) # Abc 首字母大写 其余小写

# class MyObject(object):
# 	def __init__(self):
# 		self.x = 9
# 	def power(self):
# 		return self.x * self.x

# obj = MyObject()
# print(dir(obj))
# print(hasattr(obj,'x')) # 判断obj有x属性吗 返回一个bool
# print(hasattr(obj,'y')) 

# print(getattr(obj,'x')) # 获取obj对象的x属性
# # print(getattr(obj,'y')) # 'MyObject' object has no attribute 'y' 
# print(getattr(obj,'y',404)) # 可以传入一个默认的参数,如果属性不存在,就返回默认值

# setattr(obj,'Y',19) #给obj对象 设置一个'Y'属性
# print(obj.Y)

# 
#  实例属性和类属性
# 

# class Student(object):
# 	def __init__(self,name):
# 		self.name = name

# stu = Student('Tom')
# print(stu.name)

class Student(object):
	name = "student"

s = Student() # 实例化
print(s.name) # 打印实例的name属性,但是实例里边并没有,所以回去class里边找
print(Student.name) # 打印的是类里边的属性

s.name = "Tom" # 给实例添加一个name的属性 
print(s.name) # 实例的属性优先于类属性 访问的是实例的属性,类的属性并不受影响
print(Student.name)

del s.name # 删除属性
print(s.name)


