"""
    特点：无序，唯一
    这里的无序，并不是排序的意思，而是：元素的 存， 取 顺序不一样，例如：存1，2，3 取：2，1，3
    应用场景：去重
    set1 = {值1,值2,值...}
    set2 = set()
    set3 = {}           # 不是在定义集合，而是在定义 字典

"""

set1 = {10,2,'e',5,'hsd',12,4,'f'}
set2 = set()
set3 = {}           # 不是在定义集合，而是在定义 字典

print(f'set1: {set1}')      # set1: {2, 'e', 4, 5, 10, 12, 'hsd', 'f'}
print(f'set2: {set2}')      # set2: set()
print(f'set3: {set3}')      # set3: {}

print(type(set1))       # <class 'set'>
print(type(set2))       # <class 'set'>
print(type(set3))       # <class 'dict'>

# 去重  集合具有唯一性，先转集合再转回列表
list1 = [10,20,30,20,10,30,50]
# 转集合
set_tmp = set(list1)
# 转列表
list1 = list(set_tmp)

print(f'list1: {list1}')