"""
    格式：
        with open(...) as 变量名

    在内容执行完后，自动释放资源，无需手动close
"""

# 需求：往文件1.txt中写一句话
# # 1.打开文件
# dest_f = open('./1.txt','w',encoding='utf-8')
# # 2.读写数据
# dest_f.write('好好学习天天向上')
# # 3.关闭文件,释放资源
# dest_f.close()


# with open写法
# with open('./1.txt','w',encoding='utf-8') as dest_f,open('./1.txt','r',encoding='utf-8') as src_f:
with open('./1.txt','w',encoding='utf-8') as dest_f:
    dest_f.write('好好学习天天向上')
