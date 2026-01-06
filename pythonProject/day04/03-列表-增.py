"""
    列表名.append(单个值 或者 列表)   在列表末尾添加元素，如果（添加的内容）是列表，则把列表当作1个元素来添加
    列表名.extend(列表)              在列表末尾添加元素，如果（添加的内容）是列表，则把列表中追逐个元素添加过来
    列表名.insert(索引值，要插入的元素) 在指定位置插入元素，如果索引不存在，默认往 “最后” 添加
"""

# 定义列表
list1 = [10,20,30,40,50]
list2 = ['a','b','c']
# 列表名.append(单个值 或者 列表)
list1.append('张三')
list1.append(list2)

# 列表名.extend(列表)
# list1.extend(100)       # 报错
# list1.extend(list2)

# 列表名.insert(索引值，要插入的元素)
list1.insert(2,100)       # 2在这里是正向索引  （索引值右边）
list1.insert(-2,100)             # -2在这里是逆向索引  （索引值左边）

# list1.insert(200,666)   #如果索引不存在，默认往 “最后” 添加
# list1.insert(-200,666)

# 打印
print(f'list1: {list1}')
print(f'list2: {list2}')