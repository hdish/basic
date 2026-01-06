"""
    列表名[索引] = 值            根据索引修改其对应的值
    列表名.reverse()           反转列表元素
    列表名.sort(reverse=True)  对列表元素值进行排序，reverse=False 升序，reverse=True 降序
"""
list1 = [10,20,30,10,30]

# 修改元素值
# list1[2] = 300      # 修改索引值为2的元素为：300
# list1[20] = 300     # 报错

# 反转列表元素
list1.reverse()

# 对列表元素内容排序
list1.sort()    #升序
list1.sort(reverse=False)    #效果同上，升序
list1.sort(reverse=True)    #降序

print(f'list1: {list1}')