
#!/user/bin/env python3
#_*_ coding: utf-8 _*_

#
# 模块 Module 
#
'一个测试的模块'
__author__ = 'Crazy Lin'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print("Hellow,world!")
	elif len(args) == 2:
		print("Hellow,%s!" % args[1])
	else:
		print("Too many arguments")
if __name__ == "__main__":
	test()


'下边是测试代码'

class Hellow(object):

    def hellow(self,name = "world"):
        print('hellow ,',name)


