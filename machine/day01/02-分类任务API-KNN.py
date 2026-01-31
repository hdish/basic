# 导包
from sklearn.neighbors import KNeighborsClassifier


def dm02_KNN_demo():
    # 2.获取数据
    x = [[39, 0, 31],  # 0
         [3, 2, 65],  # 1
         [2, 3, 55],  # 2
         [9, 38, 2],  # 2
         [8, 34, 17],  # 2
         [5, 2, 57],  # 1
         [21, 17, 5],  # 0
         [45, 2, 9]]
    y = [0, 1, 2, 2, 2, 1, 0, 0]

    # 3.实例化模型
    knn_cls = KNeighborsClassifier(n_neighbors=3)

    # 4.模型训练
    knn_cls.fit(x, y)

    # 5.模型预测
    print(f'预测类别：{knn_cls.predict([[23, 3, 17]])}')


if __name__ == '__main__':
    dm02_KNN_demo()
