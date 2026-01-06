# all属性 如果不写，默认是：包中所有的 模块，都不能通过from 包名 import * 的方式导入
# 会去__init__.py文件 初始化文件中，只加载all属性的信息
__all__ = ['my_module1']