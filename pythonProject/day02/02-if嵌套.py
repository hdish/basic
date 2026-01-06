money = int(input('请输入公交卡的余额'))
if money >= 2:
    print('上车')
    seat = int(input('车上有几个空位'))
    if seat > 0:
        print('入座')
else:
    print('余额不足，不能坐车')
