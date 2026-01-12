"""
加锁前的计算动作：
    1.假设g_num = 0
    2.此时线程1抢到了资源，它会去读取g_num的值 g_num=0，线程1还没有来得及计算的时候，此时被线程2抢走了资源.
    3.此时线程2也会去读取g_num的值 g_num=0，然后进行运算.
        线程1 运算：g_num=θ  g_num = 1
        线程2 运算：g_num=0  g_num = 1
    4．结论：线程1和线程2分别对g_num累加1，相当于加了2次，但是g_num最终只加了1.
"""
import threading

# 定义全局变量
g_num = 0

def get_sum1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'get_sum1函数：{g_num}')

def get_sum2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'get_sum2函数：{g_num}')

if __name__ == '__main__':
    p1 = threading.Thread(target=get_sum1)
    p2 = threading.Thread(target=get_sum2)

    p1.start()
    p2.start()