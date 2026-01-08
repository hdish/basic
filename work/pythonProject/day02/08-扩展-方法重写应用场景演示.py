"""
    子类出现和父类一模一样的方法时，称为：方法重写

    应用场景：
        子类需要沿袭父类的功能，但是功能主体又有自己独有需求的时候，就可以考虑使用方法重写了
"""

# 需求：定义手机类，有打电话的功能，定义新式手机类，重写 打电话的行为
# 1.定义手机类
class Phone(object):
    # 打电话的行为
    def call(self,name):
        print(f'-----拨号:{name}')
        print('发送信号')
        print('解析信号')
        print('接收信号')
        print('嘟嘟嘟...')

# 2.定义新式手机类
class New_Phone(Phone):
    def call(self,name):    # 子类出现和父类一模一样的方法时，称为：方法重写
        # 沿袭父类的功能
        super().call(name)
        # 功能主体有自己的需求
        print('彩铃')
        
# 在main函数中完成测试
if __name__ == '__main__':
    # 3.创建手机类对象，打电话
    p = Phone()
    p.call('帅哥')
    print('*' * 25)
    # 4.创建新手机类对象，打电话
    n = New_Phone()
    n.call('牛有道')