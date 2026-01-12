"""
默认情况下主进程会让子进程结束以后在结束

    当主进程结束让子进程同步结束：
        方式1：设置子进程为 守护进程         推荐
            子进程名.daemon = True
        特点：
            当非守护进程关闭时，它的守护进程也会同步关闭

        方式2："强制"销毁子进程
            可能会出现的问题，子进程会变成"僵尸进程"。即：资源不会被释放，而是交友 init 来维护管理，在适合的时候释放资源
            子进程 => main进程
            僵尸进程 => init进程

"""

import multiprocessing,time

def work():
    for i in range(10):
        print(f'work{i}')
        time.sleep(0.1)


if __name__ == '__main__':
    # 创建(子)进程对象，关联work()函数
    p1 = multiprocessing.Process(target=work)
    # 方式1：设置子进程为守护进程
    p1.daemon = True

    # 启动子进程
    p1.start()

    time.sleep(1)
    # 方式2：销毁子进程
    p1.terminate()

    print('main(主进程)结束')