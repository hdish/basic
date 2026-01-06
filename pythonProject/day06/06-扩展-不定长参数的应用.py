def get_sum(*args):
    # 接收所有的 位置参数，并封装成：元组,  这里直接把args当元组使用
    # 例如：args = (10,20,30)
    sum = 0
    for i in args:
        sum += i
    return sum


if __name__ == '__main__':
    result1 = get_sum(3,6)
    print(f'result1:{result1}')

    result2 = get_sum(34, 67, 2)
    print(f'result2:{result2}')

    # 可变参数最少可以传入 0个参数，最多可以传入无数个参数
    result3 = get_sum()
    print(f'result3:{result3}')