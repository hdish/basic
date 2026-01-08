"""
概述：
    在pyth中，抽象类也叫接口，指的是：有抽象方法的类，就叫抽象类
抽象方法:
    没有方法体的方法， 即：空实现的方法，用pass修饰
    例如：
        def get_sum():
            pass
    用法：
        抽象类一般充当父类，即：制定整个继承体系的 标准(规范)
        具体的实现交由 子类来完成
"""

# 需求：定义空调类(AC),制定标准：制冷，制热，摆头  两个厂商根据标准制作空调

# 1.定义空调类，制定标准
class AC(object):
    def Cold(self):
        pass
    def Hot(self):
        pass
    def Head(self):
        pass
# 2.美的空调
class Media(AC):
    def Cold(self):
        print('美的空调 制冷')
    def Hot(self):
        print('美的空调 制热')
    def Head(self):
        print('美的空调遥控摆头')

# 3.格力空调
class Gel(AC):
    def Cold(self):
        print('格力空调 制冷')
    def Hot(self):
        print('格力空调 制热')
    def Head(self):
        print('格力空调ai摆头')

if __name__ == '__main__':
    m = Media()
    m.Cold()
    m.Hot()
    m.Head()
    print('*' * 25)
    g = Gel()
    g.Cold()
    g.Hot()
    g.Head()