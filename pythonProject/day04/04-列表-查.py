"""
    列表名.index(要查找的元素，起始索引，结束索引)     类似于字符串的index（）
    列表名.count（元素值）                          统计元素在列表中出现的总次数
    元素值 in 列表名                               判断元素在不在列表中，在：True 不在：False
    元素值 not in 列表名                           判断元素在不在列表中，在：False 不在：True
"""
list1 = ['a','b','c','a','c']
# 列表名.index(要查找的元素，起始索引，结束索引)
print(list1.index('a'))                   # 0  返回第一个要查找元素的下标
print(list1.index('a',1))   # 3
# print(list1.index('a',1,3))   # 报错，包左不包右，指定区间找不到

# 列表名.count（元素值）
print(list1.count('a'))     #2

# 元素值 in 列表名
print('a' in list1)          #True

# 元素值 not in 列表名
print('a' not in list1)     #False
