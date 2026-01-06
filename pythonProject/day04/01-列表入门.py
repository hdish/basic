# 定义列表
list1 = [10,20.3,True,'abc']
list2 = list()  #空列表
list3 = []      #可以理解为 [] 是 list()的语法糖
# 打印列表
print(f'list1: {list1}')    #list1: [10, 20.3, True, 'abc']
print(f'list2: {list2}')    #list2: []
print(f'list3: {list3}')    #
# 打印列表的类型
print(type(list1))    # <class 'list'>
print(type(list2))    # <class 'list'>
print(type(list3))    # <class 'list'>
# 打印列表的某个元素
print(list1[1])         #20.3  正向索引
print(list1[-3])        #20.3  逆向索引
# 切片
print(list1[1:])       # [20.3, True, 'abc']