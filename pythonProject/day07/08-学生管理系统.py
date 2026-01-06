"""
    1.定义函数print_info(),打印提示信息
    2.自定义while True循环逻辑，实现：用户录入什么数据，就进行相应的操作
        注意：处理一下非法值
    3.自定义函数add_info(),实现：添加学生
        编号必需唯一
    4.自定义函数delete_info(),实现：删除学生
        根据编号删除(唯一)
        根据姓名删除(可重复)
    5.自定义函数update_info(),实现：修改学生信息
        根据编号修改，只能改：姓名，手机号
    6.自定义函数search_info(),实现：查询某个学生信息
        根据姓名查询(可重复)
        根据学号查询(唯一)
    7.自定义函数search_all(),实现：查询所有学生信息
    8.在main函数中，完成：程序入口启动
"""

#  1.定义函数print_info(),打印提示信息
def print_info():
    print('1.添加学生')
    print('2.删除学生')
    print('3.修改学生信息')
    print('4.查询单个学生信息')
    print('5.查询所有学生信息')
    print('6.退出查询')


# 2.自定义while True循环逻辑，实现：用户录入什么数据，就进行相应的操作
def student_manager():
    # 自定义while True循环逻辑
    while True:
        # 2.1 打印提示界面
        print_info()

        # 2.2 接收用户录入的 编号 ，注意：不要转成整数
        input_num = input('输入要执行的功能编号')

        # 2.3 判断用户的选择，并进行相应的操作
        if input_num == '1':
            # print('添加学生')
            add_info()
        elif input_num == '2':
            # print('删除学生')
            # delete_info_by_id()     # 根据学号删除(唯一)
            delete_info_by_name()     # 根据姓名删除(重复)
        elif input_num == '3':
            # print('修改学生信息')
            update_info()
        elif input_num == '4':
            # print('查询单个学生信息')
            # search_info_by_id()     # 根据学号查询(唯一)
            search_info_by_name()     # 根据姓名查询(重复)
        elif input_num == '5':
            # print('查询所有学生信息')
            search_all()
        elif input_num == '6':
            print('成功退出程序')
            break       # 结束循环
        else:
            print('输入参数有误，重新输入\n')


# 定义列表，用来记录存储所有学生信息
user_info = [
    # {'id' : '1', 'name' : '诸葛亮', 'phone' : '123'},
    # {'id' : '2', 'name' : '吕布', 'phone' : '453'},
    # {'id' : '3', 'name' : '老夫子' ,'phone' : '4563'},
    # {'id' : '3', 'name' : '老夫子' ,'phone' : '4563'},
    # {'id' : '3', 'name' : '老夫子' ,'phone' : '4563'}
]


# 3.2自定义函数add_info(),实现：添加学生
def add_info():
    # 3.3 提示用户要添加学生的学号并接收
    new_id = input('输入要添加的学号：')
    # 3.4 遍历一遍，判断要添加的学号是否存在，如果存在，提示并结束
    for stu in user_info:
        # stu的格式：{'id': '1', 'name': '诸葛亮', 'phone': '123'}
        if new_id == stu['id']:
            # 走到这说明学号重复
            print(f'学号 {new_id} 存在，请重新添加\n')
            return      # 结束函数

    # 3.5 走到在，说明学号是唯一，提示输入姓名，手机号并接收
    new_name = input('输入要修改的姓名：')
    new_phone = input('输入要修改的手机号：')

    # 3.6将用户录入的学生信息封装成字典
    new_info =  {'id' : new_id, 'name' : new_name, 'phone' : new_phone}
    # 3.7 将封装好的信息添加到学生列表中
    user_info.append(new_info)
    print(f'学号 {new_id} 添加成功\n')


# 4.自定义函数delete_info(),实现：删除学生
# 场景一：根据编号删除(唯一)
def delete_info_by_id():
    # 4.1提示用户输入要删除学生的学号并接收
    del_id = input('要删除学生的学号:')
    # 4.2遍历列表，查找有没有要删除的学号
    for stu in user_info:
        # 4.3如果有删除
        if stu['id'] == del_id:
            user_info.remove(stu)   # 具体删除学生的动作
            print(f'学号: {del_id} 删除成功\n')
            break    # 删除成功，结束循环
    # 4.4走这里，说明没有遍历循环没有break跳出，遍历一遍也没有找到要删除的学生，学号不存在
    else:
        print(f'学号 {del_id} 不存在\n')

# 场景二：根据姓名删除(可重复)
def delete_info_by_name():
    # 标记有没有删除  默认false（未删）  true（删除）
    flag = False
    # 4.1提示用户输入要删除学生的姓名并接收
    del_name = input('要删除学生的姓名:')
    i = 0
    # 4.2遍历列表，查找有没有要删除的姓名
    while i < len(user_info):
        stu = user_info[i]        # stu代表某个学生的信息
        # 4.3如果有删除
        if stu['name'] == del_name:
            user_info.remove(stu)   # 具体删除学生的动作
            flag = True
            # 删除学生后，后续的数据会向前一位，索引 -= 1 即可
            i -= 1
        # 无论有没有删除成功都进行下一个判断
        i += 1
    # 4.4走这里，通过标记判断有没有删除
    if flag == False:
        print('输入错误，没有该学生\n')
    else:
        print(f' {del_name} 删除成功\n')


# 5.自定义函数update_info(), 实现：修改学生信息
def update_info():
    # 5.1 提示用户要修改学生的学号并接收
    update_id = input('输入要修改的学号：')
    # 5.2 遍历一遍，判断要修改的学号是否存在，
    for stu in user_info:
        # stu的格式：{'id': '1', 'name': '诸葛亮', 'phone': '123'}
        if update_id == stu['id']:
            # 走到这说明学号存在，可以修改
            # 字典是可变类型的，for循环的数据是指向数据地址的，所以修改形参可以改变实参
            stu['name'] = input('输入要修改的姓名：')
            stu['phone'] = input('输入要修改的手机号：')
            print(f'学号 {update_id} 信息修改成功\n')
            break     # 结束循环
    else:
        print(f'学号 {update_id} 不存在\n')


# 6.自定义函数search_info(),实现：查询某个学生信息
# 场景一：根据学号查询(唯一)
def search_info_by_id():
    # 6.1 提示用户要查询学生的学号并接收
    search_id = input('输入要查询的学号：')
    # 6.2 遍历一遍，判断要查询的学号是否存在，
    for stu in user_info:
        # stu的格式：{'id': '1', 'name': '诸葛亮', 'phone': '123'}
        if search_id == stu['id']:
            # 走到这说明学号存在，打印信息
            print(f'{stu}\n')
            break     # 学号具有唯一性，打印完结束循环
    else:
        # 走到这说明学号不存在
        print(f'学号 {search_id} 不存在\n')


# 根据姓名查询(可重复)
def search_info_by_name():
    # 标记有没有找到  默认false（没找到）  true（找到了）
    flag = False
    # 6.1 提示用户要查询学生的姓名并接收
    search_name = input('输入要查询的姓名：')
    # 6.2 遍历一遍，判断要查询的姓名是否存在，
    for stu in user_info:
        # stu的格式：{'id': '1', 'name': '诸葛亮', 'phone': '123'}
        if search_name == stu['name']:
            # 走到这说明学号存在，打印信息
            print(f'{stu}')
            flag = True
    # if not flag:
    if flag == False:
        print(f'姓名 {search_name} 没找到\n')
    else:
        # 换行，好看一点
        print()


#  7.自定义函数search_all(),实现：查询所有学生信息
def search_all():
    if len(user_info) == 0:
        print('没有学生信息\n')
    else:
        for stu in user_info:
            print(stu)
        # 为了好看，换行
        print()


# 8.main函数 程序的主入口
if __name__ == '__main__':
    # 启动学生管理系统
    student_manager()