"""
    全称叫：Operating System,系统模块，主要是操作文件，文件夹，路径等
    属于第三方包，使用时需要导包

    常用函数：
        getcwd():获取当前的工作空间目录（即：在写相对路径时，参考的路径）current work directory
        chdir():改变工作空间路径。change directory
        rmdir():删除文件，必须是空文件夹.remove directory
        mkdir():制作文件.make directory
        rename():改名，文件名 或者文件夹名均可
        listdir():获取指定目录下所有的子集文件或者文件夹(注意：不包括子集的子集)
"""


# 导包
import os

# getcwd():获取当前的工作空间目录（即：在写相对路径时，参考的路径）current work directory
print(os.getcwd())

# chdir():改变工作空间路径。change directory
# os.chdir('d:/')
# print(os.getcwd())


# mkdir():制作文件.make directory
# os.mkdir('aa')      # 如果存在报错


# rmdir():删除文件，必须是空文件夹.remove directory
# os.rmdir('aa')


# rename():改名
# os.rename('aa','bb')
# os.rename('1.txt','qw.txt')


# listdir():获取指定目录下所有的子集文件或者文件夹(注意：不包括子集的子集)
file_list = os.listdir('./')
print(file_list)

# f = open('1.txt','r',encoding='utf-8')
# print(f.read())
# f.close()