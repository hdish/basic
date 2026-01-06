c1 = '可乐'
c2 = '牛奶'

# 方式1 采用第三方变量
tmp = c1
c1 = c2
c2 = tmp
print(f'c1:{c1},c2:{c2}')

# 方式2  python 独有
c1,c2 = c2,c1
print(f'c1:{c1},c2:{c2}')
print('-'*25)


a,b = 10,3
# 方式3 算数运算符
a = a + b    #a=13,b=3
b = a - b    #a=13,b=10
a = a - b    #a=3,b=10
