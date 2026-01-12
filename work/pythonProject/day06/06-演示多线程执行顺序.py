"""
    资源调度策略：
        均分时间片：每个线程获得的时间几乎一致
        抢占式调度：谁抢到，谁执行                   更好，充分利用cpu资源
"""

import threading,time

# 定义函数，打印当前 线程的信息
def print_info():
    # 休眠0.2秒 要不然太快没法演示抢资源
    time.sleep(0.2)
    # 获取当前正在执行的线程对象
    th = threading.current_thread()
    # 打印当前线程对象
    print(f'当前正在执行的线程是：{th}')


if __name__ == '__main__':
    # 利用for循环，创建10个线程
    for i in range(10):
        th = threading.Thread(target=print_info)

        th.start()