"""
    思路1： 根据 键 获取对应的值                理解为：根据 丈夫 找 妻子
    思路2： 根据 键值对 获取对应的 键 和 值      理解为：根据结婚证找 丈夫 和 妻子
"""
dict1 = {'乔峰':'阿朱','虚竹':'梦姑','杨过':'小龙女','郭靖':'黄蓉'}

# 思路1： 根据 键 获取对应的值
# 获取所有的键
keys = dict1.keys()
# 遍历，获取到每个键
for key in keys:
    # 2.3 根据 键 找 值
    value = dict1.get(key)
    print(f'{key} <=> {value}')
print('-' * 25)

# 简化版
for key in dict1.keys():
    print(f'{key} <=> {dict1.get(key)}')
print('-' * 25)

# 思路2： 根据 键值对 获取对应的 键 和 值
# 获取所有的 键值对 对象
items = dict1.items()
# 遍历, 获取每个键值对
for item in items:
    # print(item)     # 每个键值对:('乔峰', '阿朱')...
    # 2.3 根据 键值对 找 键和值
    key,value = item[0],item[1]
    print(f'{key} <=> {value}')

print('-' * 25)

# 简化
for item in dict1.items():
    print(f'{item[0]} <=> {item[1]}')

print('-' * 25)

# 实际开发:拆包
# 字典 中 键值对 也只有两个值
for k,v in dict1.items():       # 等价于  k , v = {'键','值'}
    print(f'{k} <=> {v}')

# 扩展：拆包写法
t1 = ('abc','bcd')
a, b = t1
print(a)
print(b)