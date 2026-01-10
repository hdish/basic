# 内部函数的形式，必须和 原函数(要被装饰的函数)形式一致，即：要有参都有惨，要有返回值都有返回值

# 定义装饰器
def peint_info(fn_name):
    def inner(a,b):     # 内部函数的形式，必须和 原函数(要被装饰的函数)形式一致
        print('计算中')
        fn_name(a,b)
    return inner

# 原函数
@peint_info
def get_sum(a,b):
    sum = a + b
    print(f'两数求和为：{sum}')

if __name__ == '__main__':
    # 正常调用原函数
    # get_sum()

    # 方法1：变量名 = 装饰器名(要被修饰的原函数名)
    # get_sum = peint_info(get_sum)
    # get_sum()

    # 写法2：语法糖     在定义原函数的时候，加上@装饰器名，之后正常调用原函数即可
    get_sum(10,3)

    print(get_sum(10,3))    # 没返回值，所有最后打印None