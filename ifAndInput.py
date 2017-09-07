
#if判断和input结合使用

# 练习
# 输入身高 格式为 175 根据用户的输入来输出高矮

userInput = input('输入你的身高:格式为175 --> : ')
#这个是写着玩儿的 并没有用上
age = input("输入年龄:")
height = int(userInput)
if height > 180 :
    print('哇哦,你真是个大个子')
elif 180 >= height >= 165 :
    print('你的身高是正常身高哦')
elif 165 > height >= 150 :
    print('你的身高还行哦,加油')
else :
    print('你现在还小,等你长大了,身高也会增长哦')

#循环 1 for in
arr = ['张三','李四','王麻子']
for name in arr :
    print(name)

sum = 0

for x in [1,2,3,4,5,6,7,8,9,10] :
    sum = sum + x
print(sum)

SUM = 0
for x in range(101) :
    SUM = SUM + x
print(SUM)

#循环 2 while

sum = 0
n = 99

while n > 0 :
    sum = sum + n
#    n = n - 2
    n -= 2
print(sum)

#
# dict - dictionary
#

d = {'张三' : 95,'李四' : 80,'王麻子' : 100}
print(d.get('王五',None)) # 如果key不存在 返回None 或者指定的value
#print(d.get('王五','这没有王五,去别家看看'))
d['王五'] = 60 #增
d.pop('王五') #删
d['张三'] = 90 #改
b = d['张三'] #查
print(b) # 95
print(d)

#
# set set和dict类似,也是一组key的集合,但不存储value.由于key不能重复,所以在set中,没有重复的key
# 要创建一个set,需要提供一个list作为输入集合:

#s = set([1,2,3,])
s = set([1,3,3,3,1,2]) # set内部会自动过滤掉重复的key
print(s)
s.add(2)
s.add(4) #增 可以重复添加,但是会被过来掉
s.remove(1) #删
print(s)
#两个set做交集
s2 = set([2,3,3,3,3,6])
print(s & s2)

list = [1,2,5,4,3,2]
list.sort()
print(list)

z = "Abc"
z.replace("A","a") # replace 是重新创建一个字符串出来 而不是改变一个字符串
print(z.replace("A","a"))
print(z)


