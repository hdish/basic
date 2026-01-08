"""
概述：
    多态是指同一个事物在不同的场景下表现出来的不同形态，状态
    python中的多态是指，同一个函数，传入不同的对象，会实现不同的结果

    多态前提条件：
        1.要有继承关系
        2.要有方法重写
        3.要有父类引用指向子类对象

    应用场景：
        父类型充当函数形参的类型，这样可以接受其任意的子类对象，实现：传入什么(子类)对象，就调用其对应的功能
"""

# 案例：动物类案例
# 1.定义动物类，有speak()函数，表示，叫
class Animal(object):
    def speak(self):
        print('动物会叫')

# 2.定义狗类，继承自动物类，重写speak()函数
class Dog(Animal):
    def speak(self):
        print('狗  汪汪汪')

# 3.定义猫类，继承自动物类，重写speak()函数
class Cat(Animal):
    def speak(self):
        print('猫  喵喵喵')

# 4.定义函数make_noise(动物类对象)，接收动物类对象，实现：传入什么动物，就怎么叫
     # an:相当于传过来的参数  Animal是父类型
def make_noise(an : Animal): # an : Animal 意思是：an"必须"是Animal类的对象或子类对象
    an.speak()      # 猫对象.speak()   狗对象.speak()

if __name__ == '__main__':
    # 分别创建猫 狗类对象
    d = Dog()
    c = Cat()
    # 调用make_noise()函数，实现：多态
    make_noise(d)
    make_noise(c)