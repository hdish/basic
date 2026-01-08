"""
方法重新：
    概述：
        子类中出现和父类一模一样的 属性 和行为(函数)时，称为：方法重新
    应用场景：
        当子类需要从父类沿袭一些功能，但是 功能主体又要有自己独立的需求时候，就可以考虑使用方法重新
"""

# 故事3：徒弟掌握的师傅和学校的技术后，有了自己的一套绝技

# 1.定义师傅类Master
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
    # 3.1属性
    def __init__(self):
        self.kongfu = '[独创摊煎饼果子技术]'

    # 3.2行为， make_cake(),表示：摊煎饼
    def make_cake(self):
        print(f'采用{self.kongfu} 制作煎饼果子')

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