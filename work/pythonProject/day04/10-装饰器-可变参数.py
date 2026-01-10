# 内部函数的形式，必须和 原函数(要被装饰的函数)形式一致，即：要有参都有惨，要有返回值都有返回值

# 案例：原函数是可变参数

# 定义装饰器
def peint_info(fn_name):
    def inner(*args,**kwargs):     # 内部函数的形式，必须和 原函数(要被装饰的函数)形式一致
        print('计算中...')
        sum = fn_name(*args,**kwargs)
        return sum      # 原函数有返回值，内部函数也要有返回值
    return inner        # 这个返回值是外部函数的

# 原函数
@peint_info
def get_sum(*args,**kwargs):
    sum = 0
    # 求所有的 位置参数的和，即：*args -> 元组
    for i in args:
        sum += i
    # 求所有的 关键字参数的和，即： **kwargs -> 字典
    for i in kwargs.values():   # kwargs.values()从字典里取值
        sum += i
    return sum      # 有返回值

if __name__ == '__main__':
    # 写法2：语法糖     在定义原函数的时候，加上@装饰器名，之后正常调用原函数即可
    print(get_sum(10,5,a=5,b=6))

