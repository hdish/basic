"""
    已知有三个教室，格式为： class_list = [[],[],[]]
    共有8名教师，格式为： name_list = [1,2,3...]
    把 8 名教师随机分配到 3个 教室中
"""
# 导包
import random

# 定于列表：教室
class_list = [[],[],[]]

# 定于列表：教师
name_list = ['萧炎','林动','牧尘','牛有道','牛有德','牛有善','刘备','关羽']

# 开始随机分配， 遍历 每个老师
for i in name_list:
    # 核心细节：随机生成教室编号，这个教室就是老师要去的教室，
    class_id = random.randint(0,2)   #包左包右
    class_list[class_id].append(i)

# 输出  方式1
# print(class_list)

# 方式2
for i in class_list:        # 遍历： 获取到每个教室的信息
    for j in i:             # 遍历： 获取到 每个教室中 每个老师 的信息
        print(j)
    print('*'*25)
