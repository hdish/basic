# 1.定义英雄1代机，战斗力：60
class HeroFlight(object):
    def power(self):
        return 60

# 2.定义英雄2代机，战斗力：80  继承自：英雄1代机
class ADvHeroFlight(HeroFlight):
    def power(self):
        return 80

# 3.定义敌机，战斗力：70
class EnemyFlight(object):
    def power(self):
        return 70

# 构建对象对战平台 object_play(英雄机，敌机)
def object_play(hf : HeroFlight,ef : EnemyFlight):
    if hf.power() > ef.power():
        print('英雄机获胜')
    else:
        print('敌机获胜')

if __name__ == '__main__':
    # 5.分别创建英雄1代机，2代机，敌机
    hf = HeroFlight()
    hf2 = ADvHeroFlight()
    ef = EnemyFlight()
    # 6.具体对战过程
    object_play(hf,ef)  # 敌机获胜
    object_play(hf2,ef) # 英雄机获胜
    object_play(hf2,hf2) #敌机获胜
    object_play(ef,hf2) # 敌机获胜
