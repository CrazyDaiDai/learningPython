
#def f(x):
#    return x * x
#
#arr = [1,2,3,4,5,6,7,8,9]
#ARR = map(f,arr)
#print(list(ARR))
##print(list(map(sum,arr)))
#print(list(map(str,arr)))

#
# sorted() 排序
#

#L = [12,341,45,23,1,423,24,53,-46,-78]
##print(sorted(L))
#print(sorted(L,key=abs)) # 可以接受另一个函数来实现自定义排序 abs->取绝对值
#print(sorted(L,key = abs,reverse = True)) #反向排序

#L = ['bob','about','Zoo','Credit']
##print(sorted(L))  # 字符的排序按照ASCll的大小比较 大写字母会排在小写字母前边
#print(sorted(L,key = str.lower)) #忽略大小写
#print(sorted(L,key = str.upper,reverse = True)) #反向排序

#L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#def get_name(arr):
#    return arr[0]
#def get_score(arr):
#    return arr[1]
#print(sorted(L,key = get_name)) # 按名字排序
#print(sorted(L,key = get_score,reverse = True)) # 按分数由高到低排序

##
## 函数作为返回值
##
#
#def lazy_sum(*args):
#    def sum():
#        ax = 0
#        for n in args:
#            ax = n + ax
#        return ax
#    return sum
#
#f = lazy_sum(1,2,3,4,5,6)
#f2 = lazy_sum(1,2,3,4,5,6)
#print(f())
#print(f == f2) # 每次调用都会返回一个新的函数,即使传入相同的参数

##
## 匿名函数 只有一些简单的情况下可以使用匿名函数
##
#
#print(list(map(lambda x : x * x,[1,2,3,4,5,6,7])))

#
# 装饰器 Decorator
#

#def now():
#    print('2017-09-11')
#f = now()
##print(f) # None 因为now()这个方法并没有返回值
#f
## 函数有个 __name__ 的属性,可以拿到函数的名字
##print(now.__name__)
#func = now
#print(func.__name__)
#
#def log(func):
#    def wrapper(*args,**kw):
#        print('call %s()' % func.__name__)
#    return wrapper
#
#@log
#def nowTime():
#    print("2017-09-11 15:39")
#
#nowTime()

#def log(text):
#    def decorator(func):
#        def wrapper(*args,**kw):
#            print("%s %s" % (text,func.__name__))
#            return func(*args,**kw)
#        return wrapper
#    return decorator
#
#@log("execute")
#def now():
#    print("2017-09-11")
#
#now()

#import functools
#
#def log(*text):
#    if len(text) > 0:
#        def decorator(func):
#            @functools.wraps(func)
#            def wrapper(*args,**kw):
#                print("方法名称 :",func.__name__,text)
#                print("开始调用")
#                f = func(*args,**kw)
#                print("结束调用")
#                return f
#            return wrapper
#        return decorator
#
#
#@log('的调用')
#def now():
#    print("2017-09-11")
#now()

#
# 偏函数(Partial function)  也是在functools模块当中提供的
#

print(int("12345",base = 10))
print(int("12345",base = 8))
print(int("12345",16))

import functools

int2 = functools.partial(int,base = 2)
print(int2("100000"))
print(int2("143",base = 10))

