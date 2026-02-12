# 1. 导入依赖包
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error  # 计算均方误差
from sklearn.model_selection import train_test_split


def dm01_模型欠拟合():
    # 2. 准备数据xy（增加上噪声）
    np.random.seed(666)  # 设置随机种子，保证结果可复现
    X = np.random.uniform(-3, 3, size=100)  # 生成100个[-3,3)之间的均匀分布随机数
    y = 0.5 * X ** 2 + X + 2 + np.random.normal(0, 1, size=100)  # 生成带噪声的二次函数数据

    # 3 训练模型
    # 3.1 实例化线性回归模型
    estimator = LinearRegression()
    # 3.2 模型训练（sklearn要求特征矩阵是二维的，所以需要reshape）
    X_reshaped = X.reshape(-1, 1)
    estimator.fit(X_reshaped, y)

    # 4 模型预测
    Y_predict = estimator.predict(X_reshaped)

    # 5 模型评估，计算均方误差
    # 5.1 模型评估MSE
    myret = mean_squared_error(y, Y_predict)
    print('均方误差(MSE)-->', myret)

    # 5.2 展示效果
    plt.scatter(X, y)  # 绘制原始数据散点图
    # 为了让拟合线更平滑，按X大小排序后绘图
    X_sorted = np.sort(X)
    Y_predict_sorted = estimator.predict(X_sorted.reshape(-1, 1))
    plt.plot(X_sorted, Y_predict_sorted, color='r')
    plt.title('线性回归拟合二次函数（欠拟合）')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.show()


# 调用函数运行
dm01_模型欠拟合()