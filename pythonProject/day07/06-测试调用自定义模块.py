"""
    1.个.py文件就可以看作是1个模块，文件名 = 模块名，所以文件名也要符合标识符的命名规范
    2.__name__在当前模块中打印的结果是__main__,在调用者模块中打印的是 当前模块名
    3.如果导入的多个模块中，有同名函数，默认会使用 最后导入的 模块的函数
    4.__all__属性只针对于 from 模块名 import * 这种写法有效，它只会导入__all__记录的内容
"""

import my_module1 as m1

# print(m1.get_sum(10,20))
# m1.fun01()
# m1.fun02()


# from my_module1 import fun01
# from my_module2 import fun01
#
# fun01()


from my_module1 import *

print(get_sum(10,20))
fun01()
fun02()