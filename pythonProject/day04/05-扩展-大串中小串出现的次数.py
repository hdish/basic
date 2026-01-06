max_str = "heimaheimawoaiheima,buguanheimahaishibaima,zhaodaogongzuojiushihaomaheimaheima"
min_str = "heima"

# 思路1：字符串自带的count（）函数
# result = max_str.count(min_str)

# 思路2：split（）切割+统计 元素个数
# list1 = max_str.split(min_str)
# result = len(list1) - 1     #分析出的规律
# print(list1)

# 思路3：替换  (大串长度-新串长度)//小串长度
# 字符串变量名.replace(旧子串，新子串，替换次数)  替换次数不写，默认替换所有
# new_str = max_str.replace(min_str,'')
# result = (len(max_str) - len(new_str)) // len(min_str)

# find() + 切片
# 字符串变量名.find(子串，起始索引，结束索引)
#         找子串在字符串中第一次出现的位置，如果写开始和结束索引（包左不包右）。就在指定区间查找找不到返回-1

result = 0
star = 0
# while True:
#     index = max_str.find(min_str,star)
#     if index == -1:     #返回-1 说明没找到
#         break
#     result += 1      #找到1次，计数+1
#     star = index + len(min_str)     # 更新起始位置

# 原理同上
# index = 0
# while index != -1:
#     index = max_str.find(min_str,star)
#     result += 1      #找到1次，计数+1
#     star = index + len(min_str)     # 更新起始位置

print(result)