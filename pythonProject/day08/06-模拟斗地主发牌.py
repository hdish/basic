# 模拟斗地主发牌

import random

# 定义变量，表示扑克牌
poker_dict = {}     # 键：牌的索引，值：具体的牌   规则：牌越小索引越小
poker_index = []    # 所有的 牌的索引，发的牌是这个，看牌是：排序后，根据键找值
p1 = []     # 玩家1
p2 = []     # 玩家2
p3 = []     # 玩家3
dp = []     # 底牌

# 1.买牌
def get_poker():
    global poker_dict
    # 定义花色列表
    color_list = ['♠','♥','♦','♣']
    # 定义数字列表
    num_list = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    # 生成 字典，键：索引，值：牌   规则：牌越小索引越小,
    # 列表 生成牌    外循环一次，内循环一圈，所以先循环数字
    # ['♠3', '♥3', '♦3', '♣3', '♠4', '♥4', '♦4', '♣4', '♠5', '♥5', '♦5'...
    poker_list = [color + num for num in num_list for color in color_list]
    # {0: '♠3', 1: '♥3', 2: '♦3', 3: '♣3', 4: '♠4', 5: '♥4'...
    poker_dict = {i : poker_list[i] for i in range(len(poker_list))}
    # 添加大小王
    poker_dict[52] = '小🤡'
    poker_dict[53] = '大🤡'
    # print(poker_list)
    # print(poker_dict)

# 2.洗牌
def shuffle_poker():
    global poker_index
    # 获取所有牌的索引
    poker_index = list(poker_dict.keys())
    # print(poker_index)

    # 具体的洗牌动作
    random.shuffle(poker_index)
    # print(poker_index)

# 3.发牌
def send_poker():
    global p1,p2,p3,dp
    # 规则：最后3张为底牌，其他轮流发
    for i in range(len(poker_index)):       # i是 打乱顺序后的牌的编号的 索引
        if i >= len(poker_index) - 3:
            dp.append(poker_index[i])
        elif i % 3 == 0:
            p1.append(poker_index[i])
        elif i % 3 == 1:
            p2.append(poker_index[i])
        else:
            p3.append(poker_index[i])

# 4.看牌
def look_poker(player_name,piayer_poker_num):
    """
    根据玩家手中牌的编号，到poker_dict中找
    :param piayer_name: 玩家名
    :param piayer_poker_num: 玩家手中牌的编号
    :return:
    """
    # 排序
    piayer_poker_num.sort()
    # 玩家手中具体的牌
    player_poker = [poker_dict[i] for i in piayer_poker_num]
    print(f'{player_name}：{player_poker}')


if __name__ == '__main__':
    # 买牌
    get_poker()
    # 洗牌
    shuffle_poker()
    # 发牌
    send_poker()
    # 看牌
    look_poker('萧炎',p1)
    look_poker('林动',p2)
    look_poker('帅哥',p3)
    look_poker('底牌',dp)