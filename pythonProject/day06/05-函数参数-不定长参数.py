"""
    python中 函数的参数有四种写法
        位置参数
        关键字参数
        默认参数(缺省参数)
        不定长参数

    细节：
        1.位置参数 和 关键字参数 是针对 实参
        2.缺省参数 和 不定长参数 是针对 形参

    不定长参数：
        不定长参数也叫 可变参数，即：参数的个数是可以变化的

    应用场景：
        适用于 实参的个数不确定的情况，就可以把 形参定义成 可变参数
    格式：
         *args          只能接收所有的 位置参数，封装到：元组中
         **kwargs       只能接收所有的 关键字参数，封装到：字典中
    细节：
            1.关于实参,位置参数在前，关键字参数在后
            2.关于形参,如果两种 可变参数都有，则：*args在前，**kwargs在后
            3.关于形参,如果有 缺省参数 又有不定长参数，则编写顺序为：*args，缺省参数，**kwargs

"""

# 1.接收位置参数
def method01(*args):            # 约定俗成，变量名可以任意写。但建议写args
    print(f'接收所有的参数为：{args}')
    print(type(args))

# 2.接收关键字参数
def method02(**kwargs):
    print(f'接收所有的参数为：{kwargs}')
    print(type(kwargs))

# 3.同时定义两种参数
#               不定长可变参数
def method03(*args,**kwargs):
    print(f'接收所有的参数为：{args}')
    print(f'接收所有的参数为：{kwargs}')

# 4.同时定义缺省参数，不定长参数
#         不定长参数  缺省参数    不定长参数
def method04(*args,name = '萧炎',**kwargs):
    print(f'name:{name}')
    print(f'接收所有的参数为：{args}')
    print(f'接收所有的参数为：{kwargs}')



if __name__ == '__main__':
    # 调用method01()函数
    method01(1,'张三',720)
   # method01(1,'张三',age = 720)     # 报错，args只能接收位置参数
    print('-' * 25)

    # 调用method02()函数
    method02(age = 1, name = '张三', phone = 720)
    print('-' * 25)

    # 调用method03()函数
    method03(10,20,name = '张三',address = '北京')
    print('-' * 25)

    # 调用method04()函数
    method04(10, 20, name='张三', address='北京')