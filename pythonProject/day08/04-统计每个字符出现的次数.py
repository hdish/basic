"""
    需求：
        键盘录入一个字符串，统计每个字符出现的次数
"""


s = input('输入字符串：')

# 定义字典，记录每个 字符 及其 次数  例如：aaabbc  'a':3,'b':2,'c':1
# word_dict = {}

# 方式1 分解版
# 遍历字符串，获取每个字符，充当字典的键
# for key in s:       # key的值： 'a','a','a','b','b','c'
#     # 核心：判断字典中是否有这个键，有就 +1 重新存储
#     if key in word_dict:
#         word_dict[key] = word_dict[key] + 1
#     else:
#         # 没有说明这个键，说明第一次出现，将其记录为1
#         # 键不存在，会自动添加该键
#         word_dict[key] = 1


# 方式2 三目运算符
# 遍历字符串，获取每个字符，充当字典的键
# for key in s:       # key的值： 'a','a','a','b','b','c'
#     word_dict[key] = word_dict[key] + 1 if key in word_dict else 1


# 方式3 字典推导式
word_dict = {key : s.count(key)  for key in s}

print(word_dict)
