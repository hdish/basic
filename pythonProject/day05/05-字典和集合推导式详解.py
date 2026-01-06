# 集合推导式

# 需求1：生成 0-9 的偶数集合
set1 = {i for i in range(10) if i % 2 == 0}
print(set1)

# 需求2：创建1个集合，数据为下方列表的2次方
list1 = [1,1,2]
set2 = {i ** 2 for i in list1}
print(set2)
print('-' * 25)

# 需求3：创建1个字典，key是 1-5 的数字，value是该数字的2次方，例如{1:2, 2:4, 3:9, 4:16, 5:25}
dict1 = {i:i ** 2 for i in range(1,6)}
print(dict1)

# 需求4：把下述两个列表，拼接成1个字典
# 两个列表元素（长度）要一致
list1 = ['name','age','gender']
list2 = ['tom','23','male']
dict2 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict2)