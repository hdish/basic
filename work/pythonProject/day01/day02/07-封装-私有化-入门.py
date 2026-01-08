"""
封装解释：
    概述：
        在python中，我们定义函数的动作，叫封装
        在python中，我们定义类，类中有属性 和 行为，这个动作也叫封装
    专业版话术：
        封装就是隐藏对象的 属性 和 实现细节，仅对外提供公共的访问方式
    问1：怎么隐藏？
    答案：私有化方式

    问2：公共的访问方式是什么？
    答案：就是自己提供对外的访问内部成员的接口

    私有化：
        概述:
            被它修饰过的内容，只能在 本类中 直接访问
        格式：
            __属性名           注意：这里是两个_
            __函数名()
        特点：
            私有化成员，子类无法继承，只能本类使用，如果子类想访问，必须通过提供的 公共访问方式(接口)


"""

# 故事6：徒弟传技术的同时，不想把私房钱也传递，制作流程也想隐藏
# 1.定义徒弟类
class Prentice(object):
    # 初始化属性
    def __init__(self):
        self.kongfu = '[独创]'
        self.__money = 10000            # 把钱私有化了

    # 行为
    def __make_cake(self):          # 方法也私有化了
        print(f'采用{self.kongfu}制作煎饼')

    # 定义公共访问接口，查看私房钱
    def see_money(self):
        return self.__money
    # 定义公共访问接口，修改私房钱
    def set_money(self,money):
        self.__money = money

    # 定义公共访问接口，调用(私有化)方法
    def make(self):
        self.__make_cake()
# 2.定义徒孙类，继承自徒弟类
class TuSun(Prentice):
    pass

if __name__ == '__main__':
    # 3.创建徒孙类对象
    t = TuSun()
    # 4.访问从父类继承过来的内容
    print(t.kongfu)
    # t.make_cake()     # 方法也私有化了
    t.make()
    # print(f'查看师傅的私房钱：{t.money}')        # 钱私有化了，访问不了
    print(f'查看师傅的私房钱：{t.see_money()}')
    t.set_money(4846415)
    print(f'查看师傅的私房钱：{t.see_money()}')
