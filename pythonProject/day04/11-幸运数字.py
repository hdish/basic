"""
    输入任意数字，然后生成1-用户录入的数字之间的列表，从中选取幸运数字（能被6整除）移动到新列表lucky，并打印两个列表
"""
# 定义列表：记录生成的数字
nums = []
# 定义列表：记录幸运数字
lucky = []

input_num = int(input('请输入1个大于等于0的整数'))

# 生成1-用户录入的数字之间的列表,然后添加到 nums 列表中
for i in range(1,input_num + 1):
    nums.append(i)

# 遍历 nums 列表，获取每个值
for i in nums:
    # 判断是否为6的倍数
    if i % 6 == 0:
        lucky.append(i)

print(f'nums: {nums}')
print(f'lucky: {lucky}')


# 合并版
nums,lucky = [],[]

# 生成1-用户录入的数字之间的列表,然后添加到 nums 列表中
for i in range(1,int(input('请输入1个大于等于0的整数')) + 1):
    nums.append(i)

# 遍历 nums 列表，获取每个值
for i in nums:
    # 判断是否为6的倍数
    if i % 6 == 0:
        lucky.append(i)

print('-' * 25)

# 合并版 推导式
# 提示用户输入值 并接收，细节：转成int类型
input_num = int(input('请输入1个大于等于0的整数'))

# 生成1-用户录入的数字之间的列表,然后添加到 nums 列表中
nums = [i for i in range(1,input_num + 1)]

# 从nums列表中，找到 幸运数字
lucky = [i for i in nums if i % 6 == 0]



print(f'nums: {nums}')
print(f'lucky: {lucky}')