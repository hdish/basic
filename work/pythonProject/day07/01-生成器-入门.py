"""
生成器介绍：
    概述：
        生成器就是用来生成数据的，用一个，生成1个，这样可以节省大量的内存空间.
    大白话解释：
        生成器的推导式写法，非常类似于以前我们用的列表，集合，字典推导式，只不过换成小括号而已.
    实现方式：
        1．推导式写法.
        2.yield关键字.
    问：如何从生成器中获取到数据？
    答：
        方式1：next（）函数，逐个获取.
        方式2：遍历生成器即可.

"""

# 回顾列表推导式
# 案例1：生成1~5的数字
list1 = [i for i in range(1,6)]
print(list1)            # [1, 2, 3, 4, 5]
print(type(list1))      # <class 'list'>

set1 = {i for i in range(1,6)}
print(set1)             # {1, 2, 3, 4, 5}
print(type(set1))       # <class 'set'>


# 案例2：演示生成器 的推导方式
typle1 = (i for i in range(1,6))   # 这个不是元组推导式，而是生成器(对象)
print(typle1)             # 地址值，生成器对象的地址。<generator object <genexpr> at 0x000002CC34D29B30>
print(type(typle1))       # <class 'generator'>
print('-'*25)


# 案例3：从生成器中获取数据
my_generator = (i for i in range(1,6))

# 方式1：
print(next(my_generator))       # 1
print(next(my_generator))       # 2
print('-'*25)

# 遍历生成器
for i in my_generator:          # 3 4 5
    print(i)