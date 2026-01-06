# 案例1：输入一个字符串，打印所有偶数位上的字符：如下标是  0，2，4，6，8...
# s1 = input('输入字符串:')
#方法1
# for i in range(0,len(s1),2):
#     print(s1[i])
#方法2
# for i in range(0,len(s1)):
#     if i % 2 == 0:
#         print(s1[i])
#方法3
s1 = input('输入字符串:')
i = 0
while i < len(s1):
    if i % 2 == 0:
        print(s1[i])
    i += 1
print('-'*25)

# 案例2：给一个文件名，判断其尾部是否以".png"结尾
file_name = 'abc.123.txt.png'
# 方法1：切片思路，只切最后4个字符
end_name = file_name[-4:]
print(end_name)
if end_name == '.png' and len(file_name) > 4:
    print('文件名是以。png结尾')
else:
    print('文件名不是以。png结尾')

# 方法2：索引方式，即rfind()找到最后一个.的索引
# num = file_name.rfind('.')
num = file_name[file_name.rfind('.'):]
print(num)
if end_name == '.png' and len(file_name) > 4:
    print('文件名是以。png结尾')
else:
    print('文件名不是以。png结尾')