# 导包
import random
# 随机生成1个 1-100之间的数
guess_num = random.randint(1,100)
# 因为不知道猜多少次那能猜对，所以用while循环，让用户一直猜
while True:
    # 提示用户录入猜的数字
    num = int(input('请输入要猜的数字：'))
    # 比较用户猜的数字和随机数
    if num < guess_num:
        print('猜小了')
    elif num > guess_num:
        print('猜大了')
    else:
        print('猜对了')
        # 核心：用户猜对了  一定要break结束循环
        break
