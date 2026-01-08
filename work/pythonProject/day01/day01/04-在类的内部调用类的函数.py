"""
    在类的内部，通过 self 关键字，访问类内部（自己的）函数

    在类中调用类的行为(函数)，通过self.的方式
"""

# 定义汽车类
class Car:
    def run(self):
        print('我是run函数')

    # 在work()函数中调用 run()函数
    def work(self):
        print('我是work函数')
        self.run()


if __name__ == '__main__':
    c1 = Car()
    c2 = Car()

    c1.run()
    c2.run()
    print('-' * 25)
    c1.work()
    c2.work()