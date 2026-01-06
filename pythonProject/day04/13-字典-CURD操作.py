"""
    增： 字典名[键名] = 值
    删： del 字典名  或者 clear（）
    改： 字典名[键名] = 值
    查： get(), keys(), values(), items()
"""
dict1 = {'杨过':'小龙女','萧炎':'林动','天':'地'}

# 增：字典名[键名] = 值
dict1['桌子'] = '板凳'      # 键不存在，就添加该键值对

# 删：del 字典名 或者 clear()
# dict1.clear()     # 清空元素
# del dict1         # 从内存中删除该字典
# del dict1['萧炎']  # 根据键，删除该键值对

# 改：字典名[键名] = 值
dict1['桌子'] = '椅子'

print(f'dict1: {dict1}')
print('-' * 25)
# 查：get(), keys(), values(), items()
# get(键,默认值)        根据键获取值，如果键不存在，就获取默认值
print(dict1.get('杨过'))             # 小龙女
print(dict1.get('杨过','张三'))       # 小龙女

print(dict1.get('乔峰'))              # None
print(dict1.get('乔峰','张三'))       # 张三
print('-' * 25)

# keys() 获取字典中所有的键
print(dict1.keys())         # dict_keys(['杨过', '萧炎', '天', '桌子'])

# values() 获取字典中所有的值
print(dict1.values())       # dict_values(['小龙女', '林动', '地', '椅子'])

# items() 把 每对键值对元素 封装成 元组，然后再放到 列表中
print(dict1.items())        # 列表 嵌套 元组 即：dict_items([('杨过', '小龙女'), ('萧炎', '林动'), ('天', '地'), ('桌子', '椅子')])