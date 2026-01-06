"""
    字符串变量名.replace(旧子串，新子串，替换次数)  替换次数不写，默认替换所有
    字符串变量名.split(切割符，切割个数)  按切割符切割字符串，切割个数表示切几个
"""
s1 = "hello and python and sql and linux"

s2 = s1.replace('and','or')            #不写个数，替换所有
s3 = s1.replace('and','or',2)  #写了个数，写了几个，替换几个

print(f's1:{s1}')      #s1（字符串）是不可变类型，内容不变
print(f's2:{s2}')
print(f's3:{s3}')

list1 = s1.split('and')
print(type(list1))          #<class 'list'>
print(list1)                #['hello ', ' python ', ' java ', ' sql ', ' scala']

list2 = s1.split('and',2)
print(type(list2))          #<class 'list'>
print(list2)                #['hello ', ' python ', ' java and sql and scala']
print('-'*25)

# 扩展 len()函数，统计字符串有几个字符
print(len(s1))
print()
print('-'*25)

# 分隔符.join（字符串）  用分隔符隔开 字符串中每个字符
s4 = 'hello'
s5 = ','.join(s4)
print(s5)       #h,e,l,l,o
print(type(s5)) #<class 'str'>

# 把'hello'=>['h','e','l','l','o']
list3 = ','.join(s4).split(',')
print(list3)   #['h', 'e', 'l', 'l', 'o']