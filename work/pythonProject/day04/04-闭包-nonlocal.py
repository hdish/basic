"""
    nonlocal 关键字介绍：
        概述：
            可以让 内部函数 去修改 外部函数的变量值
        回顾：
            global：声明变量为全局变量
            nonlocal：声明变量可以被内部函数修改
"""

def fn_outer():
    a = 100
    def fn_inner():
        # 核心细节
        nonlocal a
        a = a + 1
        print(f'a的值为：{a}')
    return fn_inner

if __name__ == '__main__':
    fn = fn_outer()

    fn()    #101
    fn()    #102
    fn()    #103