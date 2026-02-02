# 1.导入依赖包
from sklearn.preprocessing import MinMaxScaler


# 2.获取数据
x = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]

# 3.实例化模型
scaler = MinMaxScaler()

# 4.特征处理
res = scaler.fit_transform(x)

print(res)