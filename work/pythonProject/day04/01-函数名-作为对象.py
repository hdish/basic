"""
    函数名：
        函数名也可以看作是一个对象，也可以充当(实际)参数传递

        作用：
            1.充当对象，可以赋值
            2.充当实参，可以传入函数

"""

def fun1():
    print('我是fun1函数')

if __name__ == '__main__':
    # 调用 fun1() 函数
    fun1()                  # 我是fun1函数

    # 直接打印对象名
    print(fun1)             # fun1()函数在内存中的地址 <function fun1 at 0x00000242AA6361F0>
    # 打印 函数名()
    print(fun1())           # 先调用函数，因为函数无返回值，最后打印None
    # 函数名充当对象，可以赋值
    f2 = fun1               # 把 fun1 函数的地址赋值给f2
    print(f2)               # <function fun1 at 0x000001864AD961F0>
