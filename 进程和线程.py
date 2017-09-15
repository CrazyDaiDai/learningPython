
# 进程和线程

'多任务的实现有三种方式'
# 1 多进程模式
# 2 多线程模式
# 3 多进程 + 多线程模式

import os

# print('Process (%s) start...' % os.getpid())
# pid  = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
# else:
# 	print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

# pool
'如果要启动大量的子进程,可以用进程池的方式批量创建子进程'
# from multiprocessing import Pool
# import os,time,random

# #coding=utf-8

# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.' % (name,(end - start)))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Pool(9)
# 	print('Waiting for all subprocesses done...')
# 	for i in range(10):
# 		p.apply_async(long_time_task(i),args = (i,))
# 	p.close()
# 	p.join()
# 	print('All subprocesses done.')
# '上边注释掉的有点问题,以目前自己掌握的浅显知识还不能解决'

# 子进程
'subprocess 模块可以让我们非常方便的启动一个子线程,然后控制其输入和输出'

import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

'如果子进程还需要输入,则可以通过 communicate() 方法输入'

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
# output,err = p.communicate(b'set q=max\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code :',p.returncode)
# 以上并没有达到教程上的效果

'进程间通信'
# 在父进程中创建两个子进程,一个往 Queue 里写数据,一个从 Queue 里读数据 #

from multiprocessing import Process,Queue
import os,time,random
# 写数据进程执行的代码
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

# 读取数据
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	# 父进程创建queue,并传给各个子进程
	q = Queue()
	pw = Process(target = write,args = (q,))
	pr = Process(target = read,args = (q,))
	# 启动子进程pw,写入
	pw.start()
	# 启动子进程pr,读取
	pr.start()
	# 等待pw结束
	pw.join()
	# pr 进程里是死循环,无法等待其结束,只能强行终止
	pr.terminate()
