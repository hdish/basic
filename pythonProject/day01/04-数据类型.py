"""
    int     整形，整数
    float   浮点型，小数
    bool    布尔型 ，只有True和False
    str     字符串，值必须用引号包裹，单双引号均可


    list
    dict
    typle
    set

    type(变量名 或者 变量值)
"""
a = 10
b = 10.3
c = True
d = '师春'
e = '吴斤两'

# 多行字符串，必须写成三引号形式，单双引号均可
f = """
a
bc
"""
print(f)

print(a)
print(b)
# python独有，同时输出多个变量值
print(a,b,c,d,e)
# 查看数据类型
# type(变量名 或者 变量值)
print(type(20))     #<class 'int'>
print(type(a))      #<class 'int'>
print(type(b))      #<class 'float'>
print(type(c))      #<class 'bool'>
print(type(d))      #<class 'str'>
print(type(e))      #<class 'str'>
