
'Python 的內建模块 itertools 提供了非常有用的用于操作迭代对象的函数'
'无限迭代器'
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
'因为 count() 会创建一个无限的迭代器,所以上述代码会打印出自然数序列,根本停不下来'

'cycle() 会把传入的一个序列无限的重复下去'
# import itertools
# cs = itertools.cycle('Crazy') # 字符串也是序列的一种
# for str in cs:
#     print(str)
'同样是停不下来'

'repeat() 负责吧一个元素无限重复下去,不过如果提供第二个参数就可以限定重复的次数'
# import itertools
# ns = itertools.repeat('Z',10)
# for z in ns:
#     print(z)

'无限序列虽然可以无限迭代下去,但是通常我们会通过 takewhile() 等函数根据条件判断来截取出一个有限的序列'
# import itertools
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x:x <= 10,natuals)
# print(list(ns)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'chain() 可以把一组迭代器对象串联起来,形成一个更大的迭代器'
# import itertools
# for c in itertools.chain('ABC','XYZ'):
#     print(c)


'groupby() 把迭代器中相邻的重复元素挑出来放在一起'
import itertools
for key,group in itertools.groupby('AAABBBCCCDDAA'):
    print(key,list(group))
'如果要忽略大小写↓'
for key,group in itertools.groupby('AAaaAccCbbDDdAaAa',lambda str:str.upper()):
    print(key,list(group))


