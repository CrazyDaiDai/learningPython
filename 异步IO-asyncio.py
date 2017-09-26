'asyncio 是Python3.4 版本引入的标准库,直接内置了对异步IO的支持'
''' asyncio 的编程模型就是一个消息循环.我们从asyncio模型中直接获取一个 EventLoop 的引用,然后把需要执行的协程扔到EventLoop中执行,
 就实现了异步IO'''

import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again!')

# 获取 EventLoop
loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
loop.close()

