name = '萧炎'
age = 25
salary = 100.1235
flag = True

# 输出单个值
print('我的名字是：'+name)
print(age)
# print('我的年龄是:'+age)   #报错，字符串 和 整数 不能进行加法运算
print('-' * 25)
# 输出多个值
print(name,age,salary,flag)
print('-' * 25)
# 换行输出和不换行输出
print('hello')
print('world')
#上述代码完整写法
print('hello', end = '\n')  #end = '\n',程序默认添加
print('world', end = '\n')


#不换行输出
print('hello', end = '\t')
print('world')
#换行输出
print('hello\nworld', end = '\t')
print('\n')
# 格式化输出->占位符方式
print('我叫%s' %name)
print('我叫%s,今年%d岁了,工资是%f,我是帅哥吗？%s' %(name,age,salary,flag))
#占位符的特殊写法
# %5d->期望得到5位数的整数，不够前面补空格， %05d->期望得到5位数的整数，不够前面补0 %.2f->保留2位小数，会进行四舍五入
print('我叫%s,今年%5d岁了,工资是%.3f,我是帅哥吗？%s' %(name,age,salary,flag))
print('我叫%s,今年%05d岁了,工资是%.2f,我是帅哥吗？%s' %(name,age,salary,flag))
print('-' * 25)

# 格式化输出->插值表达式
print(f'我叫{name},今年{age}岁了，工资是{salary}')
print(f'我叫{name},今年{age:05d}岁了，工资是{salary:.2f}')