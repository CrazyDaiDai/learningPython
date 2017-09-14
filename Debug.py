# 
# debug 
# 

'错误处理'
'try机制'

# try:
# 	print('try...')
# 	r = 10 / 0
# 	print('resule :',r)
# except ZeroDivisionError as e:
# 	print('except :',e)
# finally:
# 	print('finally...')
# print('END')

'调试'
' 第一种方法是不断的 print 不推荐'
' 第二种方法是 assert 凡是能用 print 来辅助查看的地方都可以用 assert 来代替'

# def foo(s):
# 	n = int(s)
# 	print(n)
# 	assert n != 0,'n is zero'
# 	return 10 / n

# def main():
# 	foo('0')

# main()

'第三种是把 print 替换为 logging '

# import logging
# # logging.basicConfig(level=logging.INFO)
# # logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.DEBUG)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

'第四种是启动 python 的调试器 pdb 让程序以单步运行,可以随时查看运行状态'

                             "//最近状态老是不太好 学习效率比较低\\"

'先放一放这块的东西 等回头再来看 这个模块的知识   '




































