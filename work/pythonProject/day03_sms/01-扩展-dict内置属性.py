"""
    格式：
        对象名.__dict__
    作用：
        把对象各个属性信息，封装成 字典形式，属性名作键，属性值作值
"""

from student import Student

if __name__ == '__main__':
    # 创建学生信息
    s1 = Student('张三', '男', 23, '43534', '好')
    s2 = Student('李四', '女', 25, '234', '事发地就')

    # 需求1：把 s1 对象封装成字典形式
    # 方式1： 手动封装
    dict1 = {'name': s1.name, 'gender': s1.gender, 'age': s1.age, 'mobile': s1.mobile, 'des': s1.des}
    print(dict1)

    # 方式2： __dict__ 内置属性
    dict2 = s1.__dict__
    print(dict2)
    print('*' * 25)


    # 需求2：把[学生对象，学生对象] => [{学生对象},{学生对象}]
    student_list = [s1,s2]
    # 方式1：分解版
    list_data = []
    for stu in student_list:
        list_data.append(stu.__dict__)
    print(list_data)


    # 方式2：列表推导式
    list_data2 = [stu.__dict__ for stu in student_list]
    print(list_data2)