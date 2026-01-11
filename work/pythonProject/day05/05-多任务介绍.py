"""
多任务介绍：
    多任务指的是 多任务的执行方式，按照执行方式不同，分为：并行，并发。
    并行 和 并发的区别？
        并发：多个任务同时请求执行，但是同一瞬间，CPU只能执行1个任务，于是安安排他们交替执行，
        看起来好像是同时执行，其实不是。CPU在做着高效的切换.
        并行：多个任务同时进行，前提，需要多核CPU

    进程 和 线程：
        进程：指的是可执行程序、文件。 QQ，微信都是进程，不互享数据
        线程：指的是 进程的执行路径，执行单元

    进程介绍：
    进程指的是（Process），它是CPU分居资源的最小单位，

    多进程实现步骤：
        1.导包
            import multiprocessing
        2.创建进程对象，关联：要执行的任务(函数)
            p1 = multiprocessing.Process(target = 目标函数名)
        3.开启进程
            p1.start()
"""
# 导包
import multiprocessing
import time


def coding():
    for i in range(10):
        print('这是coding函数')
        time.sleep(0.2)         # 休眠0.2秒 要不然太快没法演示抢资源

def music():
    for i in range(10):
        print('这是music函数')
        time.sleep(0.2)         # 休眠0.2秒

if __name__ == '__main__':
    # 调用函数，如果这么写，是单进程(程序)，前边不执行完，不会走后边的
    # coding()
    # music()

    # 创建进程对象，关联上述函数
    p1 = multiprocessing.Process(target=coding)  # 目标函数名 不要加()，不然就成函数调用了
    p2 = multiprocessing.Process(target=music)

    # 开启进程
    p1.start()
    p2.start()

    for i in range(5):
        print('这是main函数')
        time.sleep(0.1)