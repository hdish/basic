"""
案例：演示 方法重写后，子类如何调用父类的 行为(函数)

问题：重写后，子类 如何访问 父类成员？
答案：
    方式1：父类名.父类方法名(self)     # self本类当前对象的引用
    方式2：super().父类方法名()

super关键字介绍：
    概述：
        它代表 本类当前对象 父类的引用
    简单理解：
        self 代表自己，super 代表父类
    细节：
        1.super()只能初始化1个父类成员，所以super写法 不适用于 多继承，更适用于 单继承
        2.在单继承中，可以把super().父类方法名(self) 简写成 super().父类方法名()
        3.多继承关系中，如果想精确的初始化某个父类的成员，要通过 父类名.父类方法名(self) 的方式实现
"""

# 故事4：顾客想吃徒弟的，也想吃师傅的

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

# 在main函数中测试
if __name__ == '__main__':
    # 4.创建徒弟类对象
    p = Prentice()
    # 5.自研
    p.make_cake()
    # 6.打印徒弟类从Master(师傅)继承过来的 行为

    p.make_master_cake()
    # 7.打印徒弟类从School(学校)继承过来的 行为
    p.make_school_cake()
    # 打印徒弟类对象 从 父类继承过来的 行为，即：旧的煎饼果子配方
    p.make_old_cake()