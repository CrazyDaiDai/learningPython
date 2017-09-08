
#
# 高级特性
#

#print('开始学习高级特性')

#
# 切片
#

#arr = [1,2,3,4,3,2,1,3,4]
#print(arr[-3:])
#print(arr[1:3])
#
#arr = list(range(0,100,2))
#print(arr)
#
##
##  迭代 iteration
##
#
#dict = {"a" : "A","b" : "B","c" : "C"}
#
#for key in dict :  # dict迭代是key
#    print(key)
#
#for k,v in dict.items() :
#    print(k,v)

#for str in "ABC" :
#    print("迭代str =",str)
#
#from collections import Iterable
#
#print(isinstance("ABC",Iterable)) #判断字符串可否可以迭代 True

#arrs = ["A","B","C","D"]
#for i,item in enumerate(arrs) :
#    print(i,item)

#arrs = [(1,1),(2,4),(3,9)]
#for x,y in arrs :
#    print(x,y)


##
## 列表生成式
##

#arrs = [x * x for x in list(range(0,101))]
#arrs = [x * x for x in list(range(0,101)) if x % 3 == 1]
#print(arrs)

## 两层

#arrs = [m + n for m in "abc" for n in "123"]
#print(arrs)

## 列出当前目录下的所有文件和目录名
#import os
#list = [l for l in os.listdir('.')]
#print(list)

## 巩固练习
#dict = {"a" : "A","b" : "B","c" : "C"}
#for key,value in dict.items() :
#    print(key,'=',value)

#arrs = ['a','b','c','d','e']
#for i,item in enumerate(arrs) :
#    print('下标为:%d' % i,'元素为:%s' % item)

## 把字符变成大写
#upperArrs = [s.upper() for s in arrs]
#print('变成大写了 :',upperArrs)
## 把字符变成小写
#lowerArrs = [s.lower() for s in upperArrs]
#print('变成小写了 ',lowerArrs)

##
## 生成器 generator
##

#arr = ["a","b","c","d","e"]
#newArr = [s + '.' for s in arr]
#print(newArr)
#generator = (s + "S" for s in arr)
##print(next(generator))
##print(next(generator))
##print(next(generator))
##print(next(generator))
##print(next(generator))
##print(next(generator)) #当没有更多元素的时候会抛出 <StopIteration> 的错误
#for g in generator :
#    print(g)

# 杨辉三角
def triangles(max):
    L = [1,]
    while len(L) - 1 < max:
        yield L
        L.append(0)
        L = [L[x] + L[x - 1] for x,y in enumerate(L)]

for L in triangles(5):
    print('#',L)
