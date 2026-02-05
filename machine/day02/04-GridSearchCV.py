# 导入工具包
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, Gridsearchcv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

# 获取数据
data = pd.read_csv('手写数字识别.csv')
x = data.iloc[:, 1:]
y = data.iloc[:, 0]

# 特征归一化【注意】
transform = MinMaxScaler()
X = transform.fit_transform(x)
# x =x / 255.

# 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                    stratify=y, random_state=22)

# 模型实例化
model = KNeighborsClassifier(n_neighbors=1)

# 网格搜索交叉验证
model = Gridsearchcv(estimator=model, param_grid={'n_neighbors': [3, 5, 7, 9, 10, 11]}, cv=4)
model.fit(x_train, y_train)
print(model.best_estimator_)

# 模型训练
model = model.best_estimator_
model.predict(x_test)

# 模型预测
img = plt.imread('demo.png')
img = img.reshape(1, -1) / 255.
print(model.predict(img))

# 模型评估
print(model.score(x_test, y_test))
