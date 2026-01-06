s = 'heima'
for i in s:
    print(i)
    if i == 'e':
        print('黑马')

# range(起始值，结束值，步长)，包左不包右，默认起始值：0，默认步长：1
# for i in range (5):    # range(0,5,1)   即(0,1,2,3,4)
# for i in range(2,5):   # range(2,5,1)   即(2,3,4)
for i in range(1, 5, 2):  # range(1,5,2)   即(1,3)

    print(i)

# for循环统计1-100之间的奇数和
sum = 0
for i in range(1, 101, 2):
    sum += i
print(f'1-100之间的奇数和为{sum}')

"""
    1：打印9*9的 矩形
    2：将上述图形改为三角形
    3：用1*3=3来代替上述的*
    4：用i和j来填充即可
"""
# for循环99乘法表
for i in range(1, 10):  # 外循环控制行
    for j in range(1, i + 1):  # 内循环控制列
        print(f'{j}*{i}={i * j}', end='\t')
    print()
