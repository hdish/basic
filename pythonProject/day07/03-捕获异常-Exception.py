"""
    格式：
        try:
            可能出现问题的代码
        except Exception as e
            出问题后的解决方法

    格式解释：
        Exception 所有异常的父类，即，它代表所有的异常
        e         类似于以前写的变量名，这里它是：异常对象名

    细节:
        还可以写成 except (异常1,异常2) as e  这种写法是捕获多种异常
"""



# 1.读取了1个不存在的文件
# scr_f = open('1.txt', 'r')      # FileNotFoundError

# 2.除0异常
# print(10 // 0)                  # ZeroDivisionError

# 3.变量未定义
# print(name)                        # NameError

# 捕获单个异常
# try:
#     # print(name)                   # NameError
#     scr_f = open('1.txt', 'r')
# except NameError as e:         # 只能捕获 NameError 异常
#     # e就是异常对象，代表着：异常信息  可以直接把它输出到控制台
#     print(e)          # name 'name' is not defined
# print('看看我执行了吗')


# # 捕获多个异常
# try:
#     # print(name)                   # NameError
#     # scr_f = open('1.txt', 'r')      # FileNotFoundError
#     print(10 // 0)                  # ZeroDivisionError
# except (NameError,FileNotFoundError) as e:         # 只能捕获 NameError 异常
#     # e就是异常对象，代表着：异常信息  可以直接把它输出到控制台
#     print(e)
# print('看看我执行了吗')

# 捕获所有异常
try:
    # print(name)                   # NameError
    # scr_f = open('1.txt', 'r')      # FileNotFoundError
    print(10 // 0)                  # ZeroDivisionError
except Exception as e:
    # e就是异常对象，代表着：异常信息  可以直接把它输出到控制台
    print(e)
print('看看我执行了吗')