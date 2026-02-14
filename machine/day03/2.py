import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge

# 1. 生成模拟数据
np.random.seed(42)
x = np.random.rand(100, 1) * 5  # (100, 1) 二维数组
y = 2 * (x**2) + 0.5 * (x**3) + np.random.randn(100, 1) * 2  # (100, 1)

# 2. 构造高次特征
x2 = x**2
x10 = np.hstack([x2, x**3, x**4, x**5, x**6, x**7, x**8, x**9, x**10])

# 3. 普通线性回归（修复维度问题）
estimator3 = LinearRegression()
estimator3.fit(x10, y)
y_predict3 = estimator3.predict(x10)  # 此时y_predict3是(100,1)

# 关键修复：对x按列排序，获取一维索引（指定axis=0）
x_sorted = np.sort(x, axis=0)  # (100,1)
idx = np.argsort(x, axis=0).ravel()  # 转为一维索引：(100,)

# 绘图：用一维索引取预测值，保证维度匹配
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.scatter(x, y, alpha=0.6, label='原始数据')
# 用idx索引后，y_predict3[idx]是(100,1)，和x_sorted维度一致
plt.plot(x_sorted, y_predict3[idx], color='r', label='普通线性回归')
plt.title('普通线性回归（无正则化）')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
print("普通线性回归系数：")
print(estimator3.coef_)

# 4. Lasso回归（L1正则，修复维度）
estimator_l1 = Lasso(alpha=0.005, normalize=True, max_iter=10000)
estimator_l1.fit(x10, y.ravel())  # y转为一维，避免维度问题
y_predict_l1 = estimator_l1.predict(x10)  # (100,) 一维数组

plt.subplot(1, 3, 2)
plt.scatter(x, y, alpha=0.6, label='原始数据')
# y_predict_l1是一维，直接用idx索引即可
plt.plot(x_sorted, y_predict_l1[idx], color='r', label='Lasso(L1)')
plt.title('Lasso回归（L1正则）')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
print("\nLasso(L1)正则回归系数：")
print(estimator_l1.coef_)

# 5. Ridge回归（L2正则，修复维度）
estimator_l2 = Ridge(alpha=0.005, normalize=True)
estimator_l2.fit(x10, y)
y_predict_l2 = estimator_l2.predict(x10)  # (100,1)

plt.subplot(1, 3, 3)
plt.scatter(x, y, alpha=0.6, label='原始数据')
plt.plot(x_sorted, y_predict_l2[idx], color='r', label='Ridge(L2)')
plt.title('Ridge回归（L2正则）')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
print("\nRidge(L2)正则回归系数：")
print(estimator_l2.coef_)

plt.tight_layout()
plt.show()