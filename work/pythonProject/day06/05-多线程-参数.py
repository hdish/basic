"""
    线程涉及的参数：
        target      当前要执行的函数
        name        设置当前进程的名字
        args        以元组的形式，给当前关联的进程传参
        kwargs      以字典的形式，给当前关联的进程传参

    细节;
        1.args方式传参，实参的 个数 和 数据类型，顺序 必须和关联函数的形参列表一致
        2.kwargs方式传参，实参的 个数 和 数据类型，必须和关联函数的形参列表一致，顺序无所谓
        3.线程的默认命名规则是：Thread-编号，编号从1开始，例如：Thread-1，Thread-2
"""

# 导包
import threading
import time


def coding(name,num):
    for i in range(num):
        print(f'{name}正在敲第{i}行代码.....')
        time.sleep(0.2)         # 休眠0.2秒 要不然太快没法演示抢资源

def music(name,count):
    for i in range(count):
        print(f'{name}正在听第{i}首歌.....')
        time.sleep(0.2)         # 休眠0.2秒

if __name__ == '__main__':
    p1 = threading.Thread(target=coding,name='张之维',args=('小明',10))  # 目标函数名 不要加()，不然就成函数调用了
    p2 = threading.Thread(target=music,name='无根生',kwargs={'count':10,'name':'小王'})

    # 开启线程
    p1.start()
    p2.start()

