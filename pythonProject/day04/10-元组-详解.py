"""
    元组属于容器的一种，属于 不可变 类型
    用小括号来表示，且元素值不可被修改

    t1 = (值1,值2,值3...)          列表：list1 = [值1,值2,值3...]
    t2 = tuple()                  列表：list2 = list()
    t3 = (值1,)

    定义元组时，如果只有1个值，则该值的末尾必须加 逗号，否则：就是在定义一个普通的变量（即：不是元组）
"""

t1 = (10,20.3,True,'abc')
t2 = tuple()
t3 = (10,)

t4 = (10)   # 它等价于 t4 = 10 这只是在定义1个普通变量，而不是定义元组
t5 = ('abc')

# 打印内容
print(t1)       # (10, 20.3, True, 'abc')
print(t2)       # ()
print(t3)       # (10,)
print(t4)       # 10
print(t5)       # abc

# 打印类型
print(type(t1))     # <class 'tuple'>
print(type(t2))     # <class 'tuple'>
print(type(t3))     # <class 'tuple'>
print(type(t4))     # <class 'int'>
print(type(t5))     # <class 'str'>
print('*' * 25)


# 和列表，字符串一样，元组也是支持函数的，例如：index(),count(),len()
t6 = ('a','b','c','d','e','b','d')

# 根据索引，获取元组的内容
print(t6.index('b'))    #1
# print(t6.index('f'))    #找不到，就报错

# count(),统计元组中元素的个数
print(t6.count('b'))    # 2

# len(),统计元组的长度，即：元组元素的个数
print(len(t6))      # 6

# 元组也支持索引，可以通过 元组名[索引]的方式获取数据
print(t6[3])        # d

# 元组和列表最大的区别：元组属于不可变类型，其元素值不能被改变
# t6[1] = 'ff'      # 报错
print(t6)