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
    细节：
        只要def函数中，看到了yield关键字，它就是生成器.
        yield关键字作用：临时存储所有的数据，并放到生成器中，调用函数时，会返回1个生成器对象.
"""

# 回顾列表推导式
# 案例1：生成1~5的数字
def get_list():
    # return [i for i in range(1,6)]        # 推导式写法

    # 分解式写法
    # 定义一个列表
    my_list = []
    for i in range(1,6):
        my_list.append(i)
    return my_list

def get_generator():
    # return (i for i in range(1,6))        # # 推导式写法,返回生成器
    for i in range(1,6):
        yield i  # 把i的每个值放到生成器中， 函数结束后，会返回：生成器对象，
                #  yieLd作用：1.创建生成器  2.把i的每个值放到生成器中  3.返回生成器


if __name__ == '__main__':
    list1 = get_list()
    generator1 = get_generator()

    print(list1)        # [1, 2, 3, 4, 5]
    print(type(list1))  # <class 'list'>

    print(generator1)           # 地址值，生成器对象的地址。<generator object get_generator at 0x000001B83E668040>
    print(type(generator1))     # <class 'generator'>

    # 遍历生成器
    for i in generator1:
        print(i)


