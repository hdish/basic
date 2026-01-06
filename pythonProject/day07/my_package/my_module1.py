# 这个是我们自定义的第1个模块

# __all__属性只针对于 from 模块名 import * 这种写法有效，它只会导入__all__记录的内容
# 如果不写all默认导入所有
__all__ = ['fun01','fun02']
# 函数 = 模块的功能，相当于：工具包中的工具

def get_sum(a,b):
    print('我是 my_module1 模块的 函数')
    return a + b



def fun01():
    print('我是 my_module1 模块的 函数')
    print('------fun01 函数------')
    print(__name__)


def fun02():
    print('我是 my_module1 模块的 函数')
    print('------fun02 函数------')
    print(__name__)


# 测试代码
# 测试代码在调用者中也会被执行，但在真实的业务场景中，测试代码在调用者中是不能被执行的
# __name__在当前模块中打印的结果是__main__,在调用者模块中打印的是 当前模块名

# print(get_sum(10,20))
# fun01()
# fun02()

# 如果条件成立，说明是在 当前模块中执行的
if __name__ == '__main__':
    print(get_sum(10, 20))
    fun01()
    fun02()