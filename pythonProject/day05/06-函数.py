"""
    1.函数必须先定义，然后才能调用
    2.定义函数小技巧，三个明确：
        明确函数名
        明确形参列表
        明确返回值
    3.调用函数三个小技巧，三个步骤
        写 函数名()
        传参， 要什么给什么，不要就不给
        接收返回值，返回什么就接收什么，不给就不接收
    4.如果函数没有明确的返回值，则return可以省略不写


    函数说明文档：在函数内部第一行  用三引号，引号可以是双引号(推荐)，也可以是单引号


    定义函数的时候，写的参数叫：形式参数
    调用函数的时候，写的参数叫：实际参数


    关于函数传递
        1.函数的返回值可以作为(另一个函数的)参数进行传递
        2.直接写函数名，是函数对象
"""

# 打印1行
def print_line(cols):      # 打印列
    for i in range(cols):
        print('-',end='')
    print()

# 打印多行
def peint_lines(row,cols):
    for i in range(row):
        print_line(cols)

peint_lines(4,7)

print('-' * 25)

# 定义函数get_sum()，用于计算三个整数的和，然后再用get_avg()函数中，调用get_sum()函数，并计算它们(三个整数)的平均值
def get_sum(a,b,c):
    return a + b + c

def get_avg(a,b,c):
    sum = get_sum(a,b,c)
    return sum / 3

print(get_avg(3,6,8))

print('-' * 25)

# 1.函数的返回值可以作为(另一个函数的)参数进行传递

def fun1():
    return 100

def fun2(num):
    print(num)

a  = fun1()

fun2(a)

fun2(fun1())

print('-' * 25)


# 2.直接写函数名，是函数对象
def sum(a,b):
    return a + b

jj = sum
"""  相当于jj变量也有了sum函数的功能
                等价于  def jj(a,b):
                           return a + b
"""