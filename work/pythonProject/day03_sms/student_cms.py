# 该文件是 学生管理系统文件，主要完成：学生管理系统的主要逻辑

# 导包
import time
from student import Student

class StudentCms(object):
    # 初始化属性，记录所有的学生信息
    def __init__(self):
        s1 = Student('张三','男',23,'43534','好')
        s2 = Student('李四','女',25,'234','事发地就')
        self.student_list = [s1,s2]  # 记录所有的学生信息

    def show_view(self):
        print('*' * 30)
        print('欢迎来到学生管理系统2.0')
        print('\t1.添加学员')
        print('\t2.修改学员')
        print('\t3.删除学员')
        print('\t4.查询某个学员')
        print('\t5.显示所有学员')
        print('\t6.保存信息')
        print('\t0.退出系统')
        print('*' * 30)

    def add_student(self):
        # 提示录入信息
        name = input('请输入要添加的学生的 姓名：')
        gender = input('请输入要添加的学生的 性别：')
        age = int(input('请输入要添加的学生的 年龄：'))  # 把年龄转换成 整数
        mobile = input('请输入要添加的学生的 手机号：')
        des = input('请输入要添加的学生的 描述信息：')

        # 把上述信息封装成对象
        stu = Student(name,gender,age,mobile,des)
        # 把封装好的学生信息添加到学生列表中
        self.student_list.append(stu)
        # 打印提示信息
        print('学生信息添加成功')

    def update_student(self):
        # 输入要修改的学生姓名
        up_name = input('要修改的学生姓名\n')
        # 遍历每个学生
        for stu in self.student_list:
            # 判断当前学生和要修改的学生是否一致
            if up_name == stu.name:
                # 如果一致，重新输入要修改的信息
                stu.gender = input('请输入要添加的学生的 性别：')
                stu.age = int(input('请输入要添加的学生的 年龄：'))  # 把年龄转换成 整数
                stu.mobile = input('请输入要添加的学生的 手机号：')
                stu.des = input('请输入要添加的学生的 描述信息：')
                print('修改信息成功\n')
                # 核心细节
                break
        # 如果循环结束，说明没有匹配到，不是以brake结束的走这
        else:
            print('没有找到\n')


    def del_student(self):
        # 输入要删除的学生姓名
        del_name = input('要删除的学生姓名\n')
        # 遍历每个学生
        for stu in self.student_list:
            # 判断当前学生和要删除的学生是否一致
            if del_name == stu.name:
                # 如果一致，删除
                self.student_list.remove(stu)
                print('删除信息成功\n')
                # 核心细节
                break
        # 如果循环结束，说明没有匹配到，不是以brake结束的走这
        else:
            print('没有找到\n')

    def search_one_student(self):
        # 输入要查找的学生姓名
        search_name = input('要查找的学生姓名\n')
        # 遍历每个学生
        for stu in self.student_list:
            # 判断当前学生和要查找的学生是否一致
            if search_name == stu.name:
                # 如果一致，打印
                print(stu,end='\n\n')
                # 核心细节
                break
        # 如果循环结束，说明没有匹配到，不是以brake结束的走这
        else:
            print('没有找到\n')

    def search_all_student(self):
        # 判断学生列表中是否有信息
        if len(self.student_list):
            # 走这里说明有信息，循环遍历
            for stu in self.student_list:
                print(stu)
            print()     # 为了好看，换行
        else:
            print('还没有信息\n')

    def save_student(self):
        # [学生对象，学生对象...] => [{学生对象}，{学生对象}...] => "[{学生对象}，{学生对象}...]" =>写到文件中
        # # 把 列表存储学生对象 转成 列表存储字典形式
        # student_dict = [stu.__dict__ for stu in self.student_list]
        # # 把上述的 列表嵌套字典 转成字符串形式
        # student_data = str(student_dict)

        # 合并版
        student_data = str([stu.__dict__ for stu in self.student_list])

        # 把上述的 信息写到文件中
        with open('./student_data.txt','w',encoding='utf-8') as dest_f:
            dest_f.write(student_data)
            print('保存成功\n')


    def load_student(self):
        # 尝试从文件中读取所有学生信息
        try:
            with open('./student_data.txt', 'r', encoding='utf-8') as src_f:
                student_data = src_f.read()
                # 判断有没有数据，没有就设置初值为："[]"
                if len(student_data) <= 0:
                    student_data = "[]"
                # list_data = list(student_data) # 这个转不了，因为是：列表嵌套字典的形式
                list_data = eval(student_data)  # eval()去掉两端的引号,是什么就是什么
                self.student_list = [Student(stu_dict['name'],stu_dict['gender'],stu_dict['age'],stu_dict['mobile'],stu_dict['des']) for stu_dict in list_data]
                                    # Student() 这个是对象， 里面的stu_dict['name']是字典键取值
        except:
            # 走这里说明文件不存在，创建即可
            dest_f = open('./student_data.txt', 'w', encoding='utf-8')
            dest_f.close()

            # pass   #直接写pass也可以
    def start(self):
        # 从文件中加载信息到student_list列表中
        self.load_student()

        while True:
            # 模拟用户等待
            time.sleep(0.5)
            # 打印登录界面
            self.show_view()
            input_num = input('请输入要操作的功能：')
            # 根据用户录入的选项，执行对应的操作
            if input_num == '1':
                self.add_student()
            elif input_num == '2':
                self.update_student()
            elif input_num == '3':
                self.del_student()
            elif input_num == '4':
                self.search_one_student()
            elif input_num == '5':
                self.search_all_student()
            elif input_num == '6':
                self.save_student()
            elif input_num == '0':
                result = input('确定要退出吗：Y/N\n')
                if result.upper() == 'Y':
                    print('再见')
                    break
            else:
                print('录入有误，重新输入')

# 测试代码
if __name__ == '__main__':
    sc = StudentCms()
    #sc.show_view()
    # print(f'目前学生信息:{sc.student_list}')

    sc.start()