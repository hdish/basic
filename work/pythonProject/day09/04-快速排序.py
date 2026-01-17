"""
快速排序：
    原理：
        找分界值，把小于分界值的数据放到分界值的左边，大于等于分界值的放到分界值的右边。
        即：小，分界值，大 这种格式.
        通过递归的思路，对于分界值两边的数据，分别可以进行排序即可。
"""


def quick_sort(my_list, start, end):
    # 1.1 如果start >= end，程序结束，说明排好顺序了.
    if start >= end:
        return  # 结束递归，即：排序成功.
    # 1.2 定义变量 left 和 right，分别表示：起始 和 结束索引
    left = start
    right = end
    # 1.3定义变量middle（mid），表示：分界值，假设：列表的第1个元素为：分界值.
    mid = my_list[start]
    # 1.4具体的排序过程，只要left<right，就说明没有找完，就一直找。
    while left < right:

        # 1.5把分界值右边比分界值小的数据放到分界值的左边.
        # 1.5.1 如果 right位置的值 比分界值大，right 就-=1
        while my_list[right] >= mid and left < right:
            right -= 1
        # 1.5.2走到这里，说明，right索引的值比分界值小，就赋值即可，即：把该值放到分界值的左边.
        my_list[left] = my_list[right]

        # 1.6把分界值左边比分界值大的数据放到分界值的右边.#1.6.1 如果left位置的值 比分界值小，left 就+=1
        while my_list[left] < mid and left < right:
            left += 1
        # 1.6.2走到这里，说明，left索引的值比分界值大，就赋值即可，即：把该值放到分界值的右边，
        my_list[right] = my_list[left]

    # 1.7 走到这里，说明 left ≥right，即：left索引的位置，就是：分界值的位置.
    my_list[left] = mid
    # 1.8走到这里，说明本轮分界值位置都已锁定，递归继续往下继续：分别对分界值左边和分界值右边的数据，做重复操作即可.
    # #1.8.1分界值左边的数据，继续排序.
    quick_sort(my_list, start, left - 1)
    # 1.8.2分界值右边的数据，继续排序.
    quick_sort(my_list, right + 1, end)


if __name__ == '__main__':
    my_list = [4,3, 5, 2, 7, 5, 4]
    print(f'排序前：{my_list}')
    quick_sort(my_list, 0, len(my_list) - 1)
    print(f'排序后：{my_list}')
