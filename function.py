
# function

#n = 255
#H = hex
#print(H(n))
#
##
## 函数定义 def 关键字
##

## 定义一个求绝对值的函数
#def my_abs(x) :
#    if x >= 0 :
#        return x
#    else :
#        return -x
#
## 函数的调用
#print(my_abs(-9))


#def my_abs(x) :
#    if not isinstance(x,(int,float)) :
#        raise TypeError('传入的类型错误')
#    if x >= 0 :
#        return x
#    else :
#        return -x
#
#print('第31行的打印',my_abs(-9))
#print(my_abs('-9'))

import math

#def move(x,y,step,angle = 0) :
#    nx = x + step * math.cos(angle)
#    ny = y - step * math.sin(angle)
#    return nx, ny
#
#print(move(100,100,60,math.pi / 6))

#def pawer(x) :
#    if not isinstance(x,(int,float)) :
#        raise TypeError('传入的类型错误')
#    return x * x
#
#print(pawer(5))

#
#  函数的参数
#

## 可变参数
#def sum(*nums) :
#    x = 0
#    for num in nums :
#        x += num
#    return x
#
#print(sum(1,2,3,4,5,3,4))

## 默认参数
#def enroll(name,sex = 0,age = 18,city = '北京') :
#    print('name =',name)
#    print('sex =',sex)
#    print('age =',age)
#    print('city =',city)
#
#enroll('三哥')
#enroll('张三',1,city = '深圳')

#def person(name,age,**kw) :
#    if 'age' in kw :
#        pass
#    if 'city' in kw :
#        pass
##        print('city :',kw['city'])
#    print('name :',name,'age :',age,'other :',kw)
#
#person('王五',28,city = '北京',addr = '朝阳',key = 'value')

#def person(name,age,*,city) :
#    print(name,age,city,job)
#
#person('z',19,city = 'beijing')

#def f1(a,b,c = 0,*nums,**kw) :
#    print(a,b,c,nums,kw)
#
#f1(1,3,4,3,23,2,2,2,3,2,2,2,2,city = 'beijing',age = 25)

def f2(a,b,c = 3,*,d,**kw) :
    print(a,b,c,d,kw)

#f2(1,2,3,d = (1,2,3,4,3,2,1,3),**{"city" : 'beijing',"key" : '朝阳群众'})
f2(1,2,3,d = (1,2,3,4,3,2,1,3),kw = {"city" : 'beijing',"key" : '朝阳群众'})
