#!/usr/bin/env python3

#定义一个变量a
a = 100
#判断a是否大于等于0
if a >= 100:
#    如果大于等于0执行这里边的内容
    print('a为正 a =',a)
else:
#    反之执行这段代码
    print('a为负 a =',a)
#
#转义字符
#

print("I'm OK")
print('I\'m OK')
print('I\'m\tlearning\nPython')
# 使用 r'' 来使 '' 里边的字符串不需要转  // 但是这样不行 --> print(r'I'm OK')
print(r'\\n\\')
# 如果有很多换行的地方可以使用 '''...''' 来表示 试了一下  这个不行
print("line1\nline2\nline3")
#print(r'line1...line2...line3')
# True  注意大小写
print(3 > 2)
# False 注意大小写
print(2 > 3)

# and or not
# and 都为真 则真 反之假
print("3 > 2 and 2 > 1 -->",3 > 2 and 2 > 1)
print("3 > 2 and 1 > 2 -->",3 > 2 and 1 > 2)
print("2 > 3 and 1 > 2 -->",2 > 3 and 1 > 2)
# or 只要一个为真 则真 反之假
print("3 > 2 or 2 > 1 -->",3 > 2 or 2 > 1)
print("3 > 2 or 1 > 2 -->",3 > 2 or 1 > 2)
print("2 > 3 or 1 > 2 -->",2 > 3 or 1 > 2)
# not 取反
print("not 3 > 2 -->",not 3 > 2)
print("not 2 > 3 -->",not 2 > 3)
#  None 在Python里边是一个特殊的值,None不能理解为0 因为0是有意义的,而None是一个特殊的空值

#
# 变量
#

a = 0
a_007 = "A_007"
answer = True
a = "ABC"

x = 2
x = x + 10
print(x)

b = a
a = "XYZ"
print(b)

#
# 在Python中通常全部大写的变量名表示常量
#

PI = 3.14159265359

#在Python中有两种除法
#1
print("10 / 3 --> ",10 / 3)
#2 --> 地板除 地板除只取结果的整数部分
print("10 // 3 --> ",10 // 3)
# 取余
print("10 % 3 -->",10 % 3)

