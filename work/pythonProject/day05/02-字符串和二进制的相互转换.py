"""
案例：演示字符串和二进制数据相互转换
背景：
    网编中，客户端和服务器端交互数据，都是采用二进制形式实现的
格式：
    字符串.encode（encoding='码表名'）          #编码，字符串 => 二进制形式，一般用：utf-8码表
    二进制字符串.decode（encoding='码表名"）    #解码，二进制字符串 => 字符串形式，一般用：utf-8码表
细节：
    1，编解码时，码表要一致，否则可能出现：乱码的情况。
    2，数字，英文字母，特殊符号，无论在什么码表中，都只占1个字节，
    中文在GBK码表（国内常用）中占2个字节，在Utf-8（万国码，统一码）码表中占3个字节
    3.b'内容'这种写法是二进制形式的字等，只针对于：字母，数字，特殊符号有效，针对于中文无效
    即：b'abc123!#' 可以，  这是直接编写二进制数据，只能字母，数字，符号，不能汉字
       b'你好'      不行，
"""
# 需求1：演示编码
s1 = '萧炎'

# 不写码表默认是：utf-8
bytes1 = s1.encode()                        # b'\xe8\x90\xa7\xe7\x82\x8e'
bytes2 = s1.encode(encoding='gbk')          # b'\xcf\xf4\xd1\xd7'
bytes3 = s1.encode(encoding='utf-8')        # b'\xe8\x90\xa7\xe7\x82\x8e'

print(bytes1)       # b'\xe8\x90\xa7\xe7\x82\x8e'
print(bytes2)       # b'\xcf\xf4\xd1\xd7'
print(bytes3)       # b'\xe8\x90\xa7\xe7\x82\x8e'

print(type(bytes1))   # <class 'bytes'>
print(type(bytes2))   # <class 'bytes'>
print(type(bytes3))   # <class 'bytes'>
print('-'* 25)
# 需求2：演示编码数字，字母
s2 = 'dg%&211'

bytes4 = s2.encode(encoding='gbk')
bytes5 = s2.encode(encoding='utf-8')
print(bytes4)           # b'dg%&211'
print(bytes5)           # b'dg%&211'
print(type(bytes4))     # <class 'bytes'>
print(type(bytes5))     # <class 'bytes'>

print(type('abc'))      # <class 'str'>
print(type(b'abc'))     # <class 'bytes'>
print('-'* 25)

# 需求3：解码
bytes1 = b'\xcf\xf4\xd1\xd7'            # 二进制形式 'gbk' 萧炎
bytes2 = b'\xe8\x90\xa7\xe7\x82\x8e'#   # 二进制形式'utf-8' 萧炎
bytes3 = b'dg%&211'                     # 啥码表都行

s1 = bytes1.decode(encoding='gbk')
s2 = bytes2.decode(encoding='utf-8')

print(s1)   # 萧炎
print(s2)   # 萧炎

print(bytes3.decode(encoding='gbk'))    # dg%&211
print(bytes3.decode(encoding='utf-8'))  # dg%&211