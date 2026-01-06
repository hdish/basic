"""
    格式：
        try:
            可能出现问题的代码
        except [Exception as e]
            出问题后的解决方法
        esle:
            只要try中无问题，就会执行这里的内容
            只要try中有问题，就会跳过这里的代码
        finally:
            无论try是否有问题，都会走这里的内容，一般用于释放资源

"""


# try:
#     print('try 1')
#     print(10 // 0)                  # ZeroDivisionError
#     print('try 2')
# except Exception as e:         # 只能捕获 NameError 异常
#     print(f'程序出问题了{e}')
# else:
#     print('我是else看看我执行了吗')
# finally:
#     print('我是finally看看我执行了吗')

print('-' * 25)

try:
    src_f = open('1.txt','rb')
    dest_f = open('ad/fef/2.txt','wb')
except Exception as e:
    print(e)
else:
    while True:
        data = src_f.read(1024)
        if len(data) <= 0:
            break
        dest_f.write(data)
finally:
    try:
        src_f.close()
    except Exception as e:
        print(e)

    try:
        dest_f.close()
    except Exception as e:
        print(e)


print('-' * 25)



try:
    with open('1.txt','rb') as src_f,open('ad/fef/2.txt','wb') as dest_f:
        while True:
            data = src_f.read(1024)
            if len(data) <= 0:
                break
            dest_f.write(data)
except Exception as e:
    print(e)