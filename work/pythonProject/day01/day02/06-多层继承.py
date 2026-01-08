"""
案例：演示 多层继承

问题：重写后，子类 如何访问 父类成员？
答案：
    方式1：父类名.父类方法名(self)     # self本类当前对象的引用
    方式2：super().父类方法名()

细节：
    1.要分清 多层继承 和 多继承
    2.多继承：1个类有多个父类
    3.多层继承：继承的传递性
"""

# 故事5：多年后，徒弟老了，把自己的独创，师傅，学校的技术传给徒孙

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

    # 3.3行为，make_master_cake(),从师傅继承过来的
    def make_master_cake(self):
        # 子类调用父类行为,方式1：父类名.父类方法名(self)
        # 初始化父类的 属性，即：调用父类的__init__()函数
        Master.__init__(self)       # 等价于做了：self.kongfu = '[古法摊煎饼果子技术]'
        Master.make_cake(self)
    # 3.4行为，make_school_cake(),从学校继承过来的
    def make_school_cake(self):
        School.__init__(self)       # 等价于做了：self.kongfu = '[黑马摊煎饼果子技术]'
        School.make_cake(self)
    # 3.3行为，make_old_cake(),从父类继承过来的
    def make_old_cake(self):
        # 子类调用父类行为，方式2：super().父类方法名()
        super().__init__()      # 初始化父类第一个成员
        super().make_cake()

class TuSun(Prentice):  # 继承关系：TuSun -> Prentice -> Master -> School -> object
    pass
# 在main函数中测试
if __name__ == '__main__':
    # 4.创建徒孙类对象,调用从父类，父类的父类 中继承过来的内容
    t = TuSun()
    t.make_cake()           # 独创
    t.make_master_cake()    # 古法
    t.make_school_cake()    # 黑马

