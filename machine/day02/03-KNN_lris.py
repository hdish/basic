from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



# 导入数据
iris_data = load_iris()

# print(f'iris_data.data[:5]: {iris_data.data[:5]}')
# print(f'iris_data.target: {iris_data.target}')
# print(f'iris_data.target_names: {iris_data.target_names}')
# print(f'iris_data.feature_names: {iris_data.feature_names}')

# 处理数据
# 把鸢尾花特征数据转成DataFrame，用特征名做列名
# iris_df = pd.DataFrame(iris_data['data'], columns=iris_data.feature_names)
iris_df = pd.DataFrame(iris_data.data, columns=iris_data['feature_names'])
# 给DataFrame新增一列'label'，赋值为鸢尾花的类别标签（0/1/2）
iris_df['label'] = iris_data.target

sns.lmplot(x='sepal length (cm)', y='petal width (cm)', data=iris_df, hue='label', fit_reg=False)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal width (cm)')
plt.show()

# 切割数据
x_train,x_test,y_train,y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=1)
print(f'x_train: {len(x_train)}')
print(f'x_test: {len(x_test)}')
print(f'iris_data.data: {len(iris_data.data)}')

# 数据预处理，
# 归一化
# scaler = MinMaxScaler(feature_range=(0,1))

# 标准化
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 模型实例化，模型训练
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

# 模型预测
# 测试集
acc = model.score(x_test,y_test)
print(f'acc: {acc}')

# 模型预测准确率
y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
print(f'acc: {acc}')



# 3. 初始化KNN模型（初始n_neighbors=1仅为占位，网格搜索会覆盖）
model = KNeighborsClassifier(n_neighbors=1)
# 4. 定义网格搜索：调优n_neighbors，4折交叉验证
estimator = GridSearchCV(estimator=model,param_grid={'n_neighbors': [4, 5, 7, 9]},cv=4)
# 5. 执行网格搜索（训练所有K值并做交叉验证）
estimator.fit(x_train, y_train)

# 6. 输出核心结果
print("交叉验证的最优平均得分：", estimator.best_score_)
print("最优参数对应的模型：", estimator.best_estimator_)
print("所有参数组合的详细交叉验证结果：\n", estimator.cv_results_)