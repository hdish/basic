class Person(object):
    # 计数器 应该共享
    count = 0       # 类变量
    # 创建对象自动调用
    def __init__(self,age,name):
        self.name = name
        self.age = age

        Person.count += 1 # 类变量的调用 类名.类属性名

    def get_num(self):
        return f'当前对象的个数为： {self.count}'

    def show_info(self):
        print('这是一个person类，谢谢查看')

    # 打印对象自动调用
    def __str__(self):
        return f'我的名字是：{self.name},年龄是{self.age}'

    # 删除对象自动调用
    def __del__(self):
        Person.count -= 1

if __name__ == '__main__':
    p1 = Person('张三',24)
    p2 = Person('李四',25)
    print(p1)
    print(f'对象个数为：{Person.count}')

    del p2

    print(f'对象个数为：{Person.count}')
