"""
插入排序：
    原理：
        相当于把列表变成有序（假设第1个元素）和 无序（第2个元素开始）两部分。
        然后从无序列表中获取每个元素，插入到有序列表中的指定位置即可，
"""
def insert_sort(my_list):
    n = len(my_list)
    # 控制轮数      假设n为5：则i的值为：1，2，3，4
    for i in range(1, n):
        for j in range(i ,0,-1):
            # 后面的值比前面的值小就交换
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            else:
                break


if __name__ == '__main__':
    my_list = [3, 5, 2, 7, 4]
    print(f'排序前：{my_list}')
    insert_sort(my_list)
    print(f'排序后：{my_list}')
