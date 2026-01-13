"""
    格式：
        1：property 充当装饰器
            @property       装修的是获取值的方法
            @方法名.setter     修饰的是设置值的方法
        2.property 充当类变量
            类变量名 = property(获取值的方法，设置值的方法)
"""

class Student(object):
    # 初始化属性
    def __init__(self):
        self.__name = ''       # 私有属性

    # 场景1：公共接口
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # property 修饰类变量
    name = property(get_name,set_name)      # 里边的函数不要加小括号


if __name__ == '__main__':
    # 创建对象
    s = Student()

    # 场景3：property 充当类变量
    # 设置值
    s.name = '诸葛青'
    # 获取值
    print(s.name)