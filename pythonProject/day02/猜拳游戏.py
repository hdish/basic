#1.导包
import random

#2.通过random.randint生成随机数  括号里直接输入取值范围
print(random.randint(1,3))  #包左包右  1-3之间的随机数
print('-'*25)

#规则   1->石头  2->剪刀  3->布
# 1.
player = int(input('输入手势编号，规则：石头（1），剪刀（2），布（3）=>'))

pc = random.randint(1,3)
#玩家胜利的情况
if (player == 1 and pc == 2 or player == 2 and pc == 3 or player == 3 and pc == 1):
    print('玩家获胜')
elif player ==pc:
    print('平局')
elif (player == 1 and pc == 3 or player == 2 and pc == 1 or player == 3 and pc == 2):
    print('电脑获胜')
else:
    print('手势有误')
