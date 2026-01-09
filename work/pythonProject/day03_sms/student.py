# 自定义 学生类 描述学生信息
class Student(object):
    def __init__(self,name,gender,age,mobile,des):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile = mobile
        self.des = des

    # 打印学生对象的各个属性
    def __str__(self):
        return f'姓名：{self.name},性别：{self.gender}, 年龄：{self.age}, 电话：{self.mobile}, 描述：{self.des}'


# 测试代码
if __name__ == '__main__':
    s = Student('阿什顿','男',23,342,'啊ui好的')
    print(s)
