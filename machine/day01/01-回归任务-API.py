# 1.导包
from sklearn.linear_model import LinearRegression


def dm01_regres():
    # 2.准备数据
    x = [[80, 86], [82, 80], [85, 78], [90, 90], [86, 82], [82, 90], [78, 80], [92, 94]]
    y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

    # 3.实例化，线性回归模型
    regression = LinearRegression()

    # 4.模型训练
    regression.fit(x, y)
    print(f'斜率：{regression.coef_}')
    print(f'截距：{regression.intercept_}')

    # 5.模型预测
    print(regression.predict([[80, 86]]))


if __name__ == '__main__':
    dm01_regres()
