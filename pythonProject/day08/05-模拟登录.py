# 用户的账号密码
username = 'daojun'
userpassword = '123'

# 因为只给三次机会，建议用for
for i in range(3):      # 0,1,2
    name = input('请输入账户：')
    password = input('请输入密码：')

    # 判断是否登陆成功，
    if name == username and password == userpassword:
        print('登录成功')
        break       # 登陆成功退出程序
    else:
        # if i == 2:
        #     print('账号锁定')
        # else:
        #     print(f'还有{2 - i}次机会')
        print('账号锁定' if i == 2 else f'还有{2 - i}次机会')

