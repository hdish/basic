"""
    len()       获取长度
    del 或者 del()      删除
    max()   获取最大值
    min()   获取最小值
    range(start,end,step) 生成指定范围内的数字
    enumerate()     基于可迭代类型(字符串，列表，元组等)，生成 下标 + 元素的方式
    即['a','b','c'] => [(0,'a'),(1,'b'),(2,'c')]
"""
list1 = [10,50,30,70,100]
# len()       获取长度
print(len(list1))

# del 或者 del()      删除
del list1[1]
del(list1[1])   # 效果同上
print(f'删除后的list1: {list1}')

# max()   获取最大值
print(f'最大值：{max(list1)}')

# min()   获取最小值
print(f'最小值：{min(list1)}')

# range(start,end,step) 生成指定范围内的数字
print(f'range生成数据：{range(1,5,2)}')  # range生成数据：range(1, 5, 2) 生成对象形式
print(f'range生成数据：{list(range(1,5,2))}')  # range生成数据：[1, 3]

# enumerate()     基于可迭代类型(字符串，列表，元组等)，生成 下标 + 元素的方式
# 即['a','b','c'] => [(0,'a'),(1,'b'),(2,'c')]
print(f'list1:{list1}')     # list1:[10, 70, 100]
print(enumerate(list1))  # 直接打印的是枚举对象的地址，无意义  <enumerate object at 0x0000013F105EB140>

for i in enumerate(list1):
    print(i)        # (0, 10)  格式：（下标，元素值）下标默认从0开始
                    # (1, 70)
                    # (2, 100)
print('-' * 25)

for i in enumerate(list1,5):
    print(i)        # (5, 10)   格式：（下标，元素值）下标从5开始
                    # (6, 70)
                    # (7, 100)

