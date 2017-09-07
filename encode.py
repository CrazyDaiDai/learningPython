#!/usr/bin/env python3

#
#字符串和编码
#

# ASCII
# Unicode
# UTF-8

# ord() --> 获取字符的整数表示 chr() 把编码转换为对应的字符
a = ord('A')
b = ord('中')

print("a =",a)
print("b =",b)

print(chr(a))
print(chr(b))

x = "中ABC国"
print(len(x))

# 格式化

x = "Tom"
y = 100
print("你好,%s.你还记得你欠我%d块钱的事情吗" % (x,y))

#转义
print('%d %%' % 7)

#
#集合
#
# 相当于Swift或者OC中的可变数组,有序的集合
classmates = ['张三','李四','王五']
# 下标  从0开始
print(classmates[0])
print(len(classmates) - 1)
print('classmates 集合的最后一个元素是:',classmates[len(classmates) - 1])
# 添加元素到集合中(加到最后)
classmates.append('马六')
# 添加元素到指定位置
classmates.insert(1,'插个班')
print(classmates)
# 移除最后一个元素
classmates.pop()
print('移除了classmates的最后一个元素',classmates)
# 移除指定位置的元素
classmates.pop(1)
print('移除了classmates中下标为1的元素',classmates)
#元素替换
classmates[0] = "尼古拉斯赵四"
print('替换classmates中下标为0的元素之后 :',classmates)
#
# tuple 不可变的数组 没有appent() insert() 方法 定义的方式为 arr = (1,2,3)
#
arr = ('a','b','c')
print(arr,arr[1])
#arr.insert(1,'这是个错误')
#这样是可以的 因为t的三个元素指向的是xy个这个集合,而xy的集合的地址没有发生变化,变化的是里边的内容
xy = ['A','B']
t = ('a','b',xy)
xy = ['X','Y']
print(t)
