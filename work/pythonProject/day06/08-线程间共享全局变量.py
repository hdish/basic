
import threading,time

# 定义全局变量
my_list = []

def write():
    for i in range(100):
        my_list.append(i)
        print(f'添加：{i}')
    print(f'write函数：{my_list}')

def read():
    print(f'read函数：{my_list}')


if __name__ == '__main__':
    p1 = threading.Thread(target=write)
    p2 = threading.Thread(target=read)

    p1.start()
    p2.start()