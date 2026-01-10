"""
    函数名：
        函数名也可以看作是一个对象，也可以充当(实际)参数传递

        作用：
            1.充当对象，可以赋值
            2.充当实参，可以传入函数

"""

def method():
    print('我是method函数')

def func(fn_nam):
    fn_nam()


if __name__ == '__main__':
    # 错误演示
    # func(10)    # 底层实际执行 10()

    # 正确演示
    func(method)    # 底层实际执行 method()