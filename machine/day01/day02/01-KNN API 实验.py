from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# 数据
# 分类
x = [[0, 2, 3], [1, 3, 4], [3, 5, 6], [4, 7, 8], [2, 3, 4]]
y = [0, 0, 1, 1, 0]
# 回归
a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
b = [0.1, 0.2, 0.3, 0.4]

# 3.实例化，线性回归模型
mode1 = KNeighborsClassifier(n_neighbors=3)
mode2 = KNeighborsRegressor(n_neighbors=3)

# 4.模型训练
mode1.fit(x, y)
mode2.fit(a, b)

# 5.模型预测
print(mode1.predict([[4, 4, 5]]))
print(mode2.predict([[4, 4, 5]]))
