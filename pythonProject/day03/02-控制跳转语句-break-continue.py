# 观察如下代码，使其能够完成 打印2次，7次，13次 hello world
for i in range(1,11):
    if i % 3 == 0:
        # break     #循环结束
        # continue  #本次循环结束，开始下次循环
        print(f'hello world {i}')
    print(f'hello world {i}')


print('至此for循环结束')