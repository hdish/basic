"""
选择排序：
    原理：
        每轮都会选出来最小值，放到最小索引处。
"""
def select_sort(my_list):
    n = len(my_list)
    # 控制轮数
    for i in range(n - 1):
        # 记录最小数的索引，默认每轮第一个值
        min_index = i
        for j in range(i + 1 , n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        # 每轮比较的循环结束，如果最小索引 不等于 默认(每轮第一个)索引，则交换
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]



if __name__ == '__main__':
    my_list = [3,5,2,7,4]
    print(f'排序前：{my_list}')
    select_sort(my_list)
    print(f'排序后：{my_list}')
