"""
    获取当前进程的id，有两种方式：
        方式1：os模块的 getpid() 函数
        方式2：multiprocessing 模块的 pid 属性
    获取当前进程的 父id：
        os模块的 getppid() 函数,         parent process,父进程
"""

# 导包
import multiprocessing
import time
import os


def coding(name, num):
    for i in range(num):
        print(f'{name}正在敲第{i}行代码...')
        time.sleep(0.2)  # 休眠0.2秒 要不然太快没法演示抢资源

        # 打印当前进程的pid                                # current_process() 获取当前正在执行的进程对象
        print(f'p1进程的id为：{os.getpid()},{multiprocessing.current_process().pid},它的父进程id为：{os.getppid()}')


def music(name, count):
    for i in range(count):
        print(f'{name}正在听第{i}首歌...')
        time.sleep(0.2)  # 休眠0.2秒
        print(f'p2进程的id为：{os.getpid()},{multiprocessing.current_process().pid},它的父进程id为：{os.getppid()}')

if __name__ == '__main__':
    # 调用函数，如果这么写，是单进程(程序)，前边不执行完，不会走后边的
    # coding()
    # music()

    # 创建进程对象，关联上述函数
    p1 = multiprocessing.Process(target=coding, name='张之维', args=('小明', 10))  # 目标函数名 不要加()，不然就成函数调用了
    p2 = multiprocessing.Process(target=music, name='无根生', kwargs={'count': 10, 'name': '小王'})

    # # 打印进程的名字,没有设置名字之前
    # print(f'p1进程的名字：{p1.name}')     # p1进程的名字：Process-1
    # print(f'p2进程的名字：{p2.name}')     # p2进程的名字：Process-2

    # 打印进程的名字,设置名字之后
    # print(f'p1进程的名字：{p1.name}')    # p1进程的名字：张之维
    # print(f'p2进程的名字：{p2.name}')    # p2进程的名字：无根生

    # 开启程序
    p1.start()
    p2.start()