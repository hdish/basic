"""
多线程实现步骤：
        1.导包
            import threading
        2.创建线程对象，关联：要执行的任务(函数)
            p1 = threading.Thread(target = 目标函数名)
        3.开启线程
            p1.start()
"""

import threading,time

def coding():
    for i in range(10):
        print('这是coding函数....')
        time.sleep(0.2)         # 休眠0.2秒 要不然太快没法演示抢资源

def music():
    for i in range(10):
        print('这是music函数...')
        time.sleep(0.2)         # 休眠0.2秒

if __name__ == '__main__':
    p1 = threading.Thread(target=coding)  # 目标函数名 不要加()，不然就成函数调用了
    p2 = threading.Thread(target=music)

    p1.start()
    p2.start()

