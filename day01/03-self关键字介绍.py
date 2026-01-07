"""
    self关键字介绍
        谁调用这个函数，self就代表谁
"""
# 创建汽车类Car，分别创建两个对象，观察结果
class Car:
    # 定义行为，跑
    def run(self):
        print('汽车会跑')
        print(f'self:{self}')


if __name__ == '__main__':
    # 创建对象
    c1 = Car()
    c2 = Car()

    # 调用类的成员
    c1.run()
    c2.run()
    print('-' * 25)
    
    # 打印对象名
    print(c1)   # <__main__.Car object at 0x000002034481A670>
    print(c2)   # <__main__.Car object at 0x000002034481A5B0>
