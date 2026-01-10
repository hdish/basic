"""
    一个装饰器的 参数 只能有 1个
"""


# 定义1个既能装饰 加法运算， 又能装饰减法运算
# 传入 add() 函数就提示加法运算， 传入 substract() 函数提示减法运算

def logging(flag):
    def print_info(fn_name):     # 这个才是装饰器，因为装饰器的参数只能有1个，所以在外面再包裹一层，专门用于传参数
        def inner(a,b):
            if flag == '+':
                print('加法运算')
            elif flag == '-':
                print('减法运算')
            fn_name(a,b)
        return inner
    return print_info

@logging('+')
def add(a, b):
    result = a + b
    print(result)

@logging('-')
def substract(a, b):
    result = a - b
    print(result)


if __name__ == '__main__':
    add(10,2)
    substract(10,2)