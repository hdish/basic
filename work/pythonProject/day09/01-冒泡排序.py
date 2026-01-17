"""
冒泡排序：
    原理：
        相邻元素两两比较，大的往后走，这样第一轮比较完毕后，最大值就在最大索引处。
"""

def bublle_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):       # 控制轮数
        count = 0                # 记录每轮交换的次数
        for j in range(n - 1 - i):   # 控制每轮比较的次数
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                count += 1
        if count == 0:  # 说明没有发生交换，即，已经是有序的了
            break


if __name__ == '__main__':
    my_list = [3,5,2,7,4]
    print(f'排序前：{my_list}')
    bublle_sort(my_list)
    print(f'排序后：{my_list}')
