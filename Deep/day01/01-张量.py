import torch
import numpy as np

# data = torch.randn(4,5)
# print(data)
#
# print(torch.zeros(2,3))
# print(torch.zeros_like(data))
# print(torch.ones(2,3))
# print(torch.ones_Like(data))
# print(torch.full([2, 3],100))
# print(torch.full_like(data,1oo))



data = torch.full([2, 3],10)
print (data.dtype)
#将data 元素类型转换为 float64 类型
data =data.double()
print (data.dtype)
#转换为其他类型
# data = data.short()
# data = data.int()
# data = data.long()
# data = data.float()

#1.将张量转换为 numpy 数组
data_tensor = torch.tensor([2, 3, 4])
#使用张量对象中的 numpy 函数进行转换
data_numpy = data_tensor.numpy()
print(type(data_tensor))
print(type(data_numpy))

#注意：data_tensor 和 data numpy 共享内存
#修改其中的一个，另外一个也会发生改变
# data_tensor[o] = 100
data_numpy[0] = 100
print(data_tensor)
print(data_numpy)


#2.对象拷贝避免共享内存
data_tensor = torch.tensor([2, 3, 4])
#使用张量对象中的numpy 函数进行转换，通过copy方法拷贝对象
data_numpy = data_tensor.numpy(). copy()
print(type(data_tensor))
print (type (data_numpy))

#注意：data_tensor 和 data_numpy 此时不共享内存
#修改其中的一个，另外一个不会发生改变
# data_tensor[0] = 100

data_numpy[0] = 100
print(data_tensor)
print(data_numpy)