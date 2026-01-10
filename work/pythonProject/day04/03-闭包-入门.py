"""
    闭包：
        格式：
            def 外部函数名(形参列表):
                可以定义 外部函数的 局部变量
                def 内部函数名(形参列表)
                    在这里使用外部函数

                return 内部函数名

        作用：
            可以保存外部函数变量，即：外部函数执行结束后，它的变量也可以在 内部函数中 使用
    闭包的三个条件：
        1.有嵌套，即：有外部函数，有内部函数
        2.有引用,即：在内部函数中，使用外部函数变量
        3.有返回，即：在外部函数中，返回 内部函数(对象)
"""

def method():
    a = 10
    return a

def outer(num1):
    def inner(num2):            # 有嵌套
        sum = num1 + num2       # 有引用
        print(f'求和结果为: {sum}')
    return inner                # 有返回


if __name__ == '__main__':
    print(method())  # 10

    print(method() + 1)  # 11
    print(method() + 1)  # 11
    print(method() + 1)  # 11

    fn = outer(10)  # 传回来inner这个内部函数对象(地址值) 这行代码走完，外部函数就执行结束了
    print(fn)       #  <function outer.<locals>.inner at 0x000001E77E002A60>
    fn(1)       # 11
    fn(1)       # 11
    fn(1)       # 11
