"""
    捕获异常这种方式处理完异常之后，程序会 自动往下 继续执行
    (基本)格式:
        try:
            可能出现问题的代码
        except：
            出问题后的解决方法

    具体流程:
        1.先执行try中的内容，看有无问题，有问题会 立即 跳转到 except中执行
        2.如果try中内容无问题，程序会跳过 except，继续向下执行
"""


# 演示try。except写法
try:
    print('try 1')
    # 1.读取了1个不存在的文件
    scr_f = open('1.txt','r')
    print('try 2')
except:
    print('文件不存在，请重新操作')


# 2.除0异常
# print(10 // 0)


print('看看我执行了吗')