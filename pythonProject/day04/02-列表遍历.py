# 定义列表
list1 = [11,22,33,44,55]

# 遍历列表
# 思路1：采用for循环
for i in list1:
    print(i)
print('-' * 25)
# 思路2：采用 索引的 方式，while循环


i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print('-' * 25)

# 思路2：采用 索引的 方式，for循环
# range(起始值，结束值，步长)，包左不包右，默认起始值：0，默认步长：1
for i in range(len(list1)):
    print(list1[i])