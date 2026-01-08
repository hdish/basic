# 单继承指的是：类只能继承自另外1个类，从中继承过来 属性 和 行为

# 故事1：一个摊煎饼的老师傅，研发了一套绝技，老师傅传授这套技术给徒弟
# 1.定义师傅类Master
class Master(object):
    # 1.1属性 kongfu = '[古法摊煎饼果子技术]'
    def __init__(self):
        self.kongfu = '[古法摊煎饼果子技术]'

    # 1.2行为， make_cake(),表示：摊煎饼
    def make_cake(self):
        print(f'采用{self.kongfu} 制作煎饼果子')


# 2.定义徒弟类Prentice，继承自师傅类
class Prentice(Master):
    pass

# 在main函数中测试
if __name__ == '__main__':
    # 3.创建徒弟类对象
    p = Prentice()
    # 4.通过徒弟类对象，调用师傅类(父类)中继承过来的 属性 和行为
    print(f'徒弟从师傅继承过来的属性： {p.kongfu}')
    p.make_cake()   # 徒弟从师傅继承过来的行为