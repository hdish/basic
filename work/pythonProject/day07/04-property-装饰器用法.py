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

    # # 场景1：公共接口
    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, name):
    #     self.__name = name

    # # 场景2：私有属性 property 充当装饰器
    # @property
    # def get_name(self):
    #     return self.__name
    # @get_sum.setter
    # def set_name(self,name):
    #     self.__name = name

    # 场景2.1：property 充装饰器 结合 get_xxx,set_xxx最终写法
    @property
    def name(self):             # 把公共类函数名写成name
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


if __name__ == '__main__':
    # 创建对象
    s = Student()

    # # 场景1：私有属性 通过公共接口来访问
    # # 设置值
    # s.set_name('张之维')
    # #获取值
    # print(s.get_name())

    # # 场景2：私有属性 property 充当装饰器
    # # 设置值
    # s.set_name = '无根生'
    # #获取值
    # print(s.get_name)

    # 场景2.1：property 充当装饰器，最终写法
    # 设置值
    s.name = '王也'
    # 获取值
    print(s.name)