"""
    1.必须使用通一把锁，否则可能出现锁不住情况
    2.用完后一定要释放锁，否则可能造成"死锁"
"""
import threading

# 定义全局变量
g_num = 0


# 核心细节，加一把锁
mutex = threading.Lock()

def get_sum1():
    # 加锁
    mutex.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'get_sum1函数：{g_num}')
    # 释放锁
    mutex.release()

def get_sum2():
    # 加锁
    mutex.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'get_sum2函数：{g_num}')
    # 释放锁
    mutex.release()

if __name__ == '__main__':
    p1 = threading.Thread(target=get_sum1)
    p2 = threading.Thread(target=get_sum2)

    p1.start()
    p2.start()