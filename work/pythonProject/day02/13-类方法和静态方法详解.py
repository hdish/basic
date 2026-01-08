"""
    类方法 和 静态方法详解：
    概述：
        类方法：
            1.第1个参数必须是 当前类的对象，一般用 cls当作变量名(即：class)
            2.类方法必须通过 @classmethod来修饰
            3.类方法是属于 类的方法，能被该类下所以的对象共享
            4.可以通过 类名. 或者 对象名. 的方式调用，推荐:前者
        静态方法：
            1.静态方法没有参数的硬性要求，可以1个参数都不传
            2.静态方法必须通过@staticmethod来修饰
            3.类方法是属于 类的方法，能被该类下所以的对象共享
            4.可以通过 类名. 或者 对象名. 的方式调用，推荐:前者

    区别：
        类方法 和 静态方法的区别：要不要传参，即：第一个参数是 写 还是 不写，
        再简单点说：是否需要使用该类的对象，用就定义成 类方法，不用就定义成 静态方法
"""

# 定义学生类
class Student(object):
    # 老师的名字
    teacher_name = '高帅峰'    # 类属性，每个对象所共享

    # name属性，每个学生的名字都不一样，所以定义成：对象属性
    def __init__(self):
        self.name = '张三'

    # 定义静态方法，访问 teacher_name 这个变量
    @staticmethod
    def method1():
        print(Student.teacher_name) # 类名.的方式，访问：类变量

    # 定义类方法，访问 teacher_name 这个变量
    @classmethod
    def method2(cls):   # 这里的cls是class的意思
        print(cls.teacher_name)

if __name__ == '__main__':
    s = Student
    s.method1()          # 对象名.类属性名       # 可以用，但不推荐
    Student.method1()    # 类名.类属性名         # 推荐使用
    Student.method2()    # 类名.类属性名         # 推荐使用