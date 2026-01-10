"""
    多个装饰器装饰1个函数：
        1.多个装饰器 装饰1个函数，装饰的顺序是 由内向外的     # 即：传统写法
        2.但是多个装饰器的执行顺序是，由上往下的             # 即：语法糖写法

"""

# 需求：发表评论前，先登录再验证，再不改变原有函数的基础上，对代码增强

# 定义装饰器，加入：登录功能
def check_user(fn_name):
    def inner():
        print('登录中...')
        fn_name()
    return inner

# 定义装饰器，加入：验证功能
def check_code(fn_name):
    def inner():
        print('验证...')
        fn_name()
    return inner

# 原函数
# @check_user
# @check_code
def comment():
    print('发表评论')

if __name__ == '__main__':
    # 传统写法    由内向外装饰
    # 目前函数的关系，由内向外分别是： comment() -> check_code() -> check_user()
    cc = check_code(comment)
    comment = check_user(cc)
    comment()


    # 语法糖       由上往下执行
    # comment()

