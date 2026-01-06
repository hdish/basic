"""

"""
name_list1 = [['萧炎','林动','牧尘'],['牛有道','牛有德','牛有善'],['刘备','关羽','张飞']]

print(name_list1[1])         # ['牛有道', '牛有德', '牛有善']
print(name_list1[1][0])      # 牛有道
print(name_list1[2][1])      # 关羽
print('-'*25)

# 遍历 方法1
for i in range(len(name_list1)):
    # i 代表的是二维列表的每个元素的 索引
    new_list = name_list1[i]      # ['萧炎','林动','牧尘']
    # 因为 new_list 还是一个列表，接着遍历
    for j in range(len(new_list)):
        print(new_list[j])
    print('-'*25)

print('*'*25)

# 方法2
for i in name_list1:
    for j in i:
        print(j)
    print('#'*25)
