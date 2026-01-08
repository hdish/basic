"""
多继承 细节：
    1.python中一个类可以继承多个父类，写法格式： class 子类名(父类1,父类2...):
    2.如果1个类继承了多个父类，则该子类可以拥有所有父类的 属性 和行为。        前提：父类的私有成员除外
    3.如果1个类继承了多个父类，且多个父类有相同的 属性 和 行为，优先参考 第一个 父类的内容，这个是根据MRO规则实现的
    4.MRO 全称是 Method Resolution Order,方法解析顺序，它规定了继承关系中，属性和行为的 查找顺序，即：先找谁，后找谁
        调用方式如下：
            类名.__mro__      属性的方式调用
            类名.mro()        行为(函数)的方式调用
"""
# 故事1：徒弟好学，又去学校学习
# 2.定义师傅类Master
class Master(object):
    # 1.1属性 kongfu = '[古法摊煎饼果子技术]'
    def __init__(self):
        self.kongfu = '[古法摊煎饼果子技术]'

    # 1.2行为， make_cake(),表示：摊煎饼
    def make_cake(self):
        print(f'采用{self.kongfu} 制作煎饼果子')

# 2.定义学校School
class School(object):
    # 2.1属性 kongfu = '[黑马摊煎饼果子技术]'
    def __init__(self):
        self.kongfu = '[黑马摊煎饼果子技术]'

    # 2.2行为， make_cake(),表示：摊煎饼
    def make_cake(self):
        print(f'采用{self.kongfu} 制作煎饼果子')

# 3.定义徒弟类Prentice，继承自师傅类
class Prentice(Master,School):       # 有多个父类有相同的 属性 和 行为，优先参考 第一个 父类的内容，从左往右
    pass

# 在main函数中测试
if __name__ == '__main__':
    # 4.创建徒弟类对象
    p = Prentice()
    # 5.打印徒弟类从父类继承过来的 属性
    print(p.kongfu)
    # 6.打印徒弟类从父类继承过来的 行为
    p.make_cake()
    # 7.MRO规则
    print(Prentice.__mro__)
    print(Prentice.mro())
