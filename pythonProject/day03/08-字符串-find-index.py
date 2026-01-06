"""
    字符串变量名.find(子串，起始索引，结束索引)
        找子串在字符串中第一次出现的位置，如果写开始和结束索引（包左不包右）。就在指定区间查找找不到返回-1
    字符串变量名.index(子串，起始索引，结束索引)
        效果同上，只不过找不到就报错

    字符串变量名.rfind(子串，起始索引，结束索引)
        效果类似于find（），只不过是找最后一次出现的地方
    字符串变量名.rindex(子串，起始索引，结束索引)
        效果同上，只不过找不到就报错
"""
s1 = "hello and python and java and sql and scala"
print(s1.find('and'))                         #6
print(s1.find('and',7,30)) #17
print(s1.find('and',7,19)) #-1 包左不包右，取不到索引19
print('-'*25)
print(s1.index('and'))                         #6
print(s1.index('and',7,30)) #17
# print(s1.index('and',7,19)) #报错
print('-'*25)

print(s1.rfind('and'))                         #34
print(s1.rfind('and',10,30)) #26
print(s1.rfind('and',10,19)) #-1 包左不包右，取不到索引19
print('-'*25)

print(s1.rindex('and'))                         #34
print(s1.rindex('and',10,30)) #26
# print(s1.rindex('and',10,19)) #报错