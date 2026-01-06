"""
    格式：
        while 或者 for循环：
            循环体
        else：
            语句体

    只要循环不是break方式跳出的，就会走else的内容，否则不执行else的内容
"""
for i in range(1,11):
    if i % 3 == 0:
        continue
        # break
    print(f'hello world {i}')
else:
    print('我是else，看看我执行了吗')


