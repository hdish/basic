"""
    方式1：创建线程时，daemon属性实现          #进程是创建后设置，线程是创建中设置
    方式2：线程对象名.setDaemon() 函数实现
"""

import threading,time

def work():
    for i in range(10):
        print(f'work{i}')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建(子)线程对象，关联work()函数
    # p1 = threading.Thread(target=work)
    # 方式1：demon属性实现,  进程是创建后设置，线程是创建中设置
    # p1 = threading.Thread(target=work,daemon=True)

    # 方式2：销毁子进程
    p1 = threading.Thread(target=work)
    p1.setDaemon(True)

    # 启动子进程
    p1.start()

    time.sleep(1)
    print('main(主线程)结束')