"""
    python的特有写法
    列表推导式： 变量名 = [变量名 for ... in ... if 判断条件]
    集合推导式： 变量名 = {变量名 for ... in ... if 判断条件}
    字典推导式： 变量名 = {变量名1：变量名2 for ... in ... if 判断条件}
"""
# 需求1：创建1个 0-9的列表
# 方法1：不使用推导式
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# 方法2： 推导式
list2 = [i for i in range(10)]
print(list2)

# 方法3： 类型转换
list3 = list(range(10))
# list3 = range(10)  # range(0, 10)
print(list3)
print('-' * 25)

# 需求2：创建1个 0-9的 偶数列表
# 方法1：不使用推导式
list1 = []
for i in range(10):
    if i % 2 == 0:
        list1.append(i)
print(list1)

# 方法2： 推导式
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)

# 需求3：创建列表 => [(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
# 循环嵌套  i的值：1，2  j的值：0，1，2
# 方法1：普通版，循环嵌套
list1 = []
for i in range(1,3):
    for j in range(3):
        # # 分解步骤
        # # 把i和j封装成元组
        # tuple1 = (i,j)
        # # 把封装好的元组添加到列表里
        # list1.append(tuple1)
        list1.append((i,j))
print(list1)

# 方法2：推导式
list2 = [(i,j) for i in range(1,3) for j in range(3)]   # 效果同上
print(list2)