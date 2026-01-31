# 导包
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import calinski_harabasz_score
import matplotlib.pyplot as plt


def dm03_kmean_demo():
    # 2.创建数据
    # x：特征数据，形状为(1000, 2)，表示 1000 个样本，每个样本有 2 个特征（对应平面直角坐标系的 x、y 轴，方便绘图）；
    # y：真实聚类标签（代码里没用到，因为 KMeans 是无监督学习，不需要真实标签，仅用于生成数据时的聚类划分）。
    # n_samples=1000	生成的样本总数	共 1000 个数据点
    # n_features=2	每个样本的特征数	2 个特征→平面绘图，直观可见
    # centers	聚类中心的坐标	设置 4 个中心：(-1,-1)、(0,0)、(1,1)、(2,2)，即数据天然分为 4 簇
    # cluster_std	每个聚类的标准差	数值越小，簇内数据点越集中；本次第 1 簇 (std=0.4) 稍分散，后 3 簇更集中
    # random_state=11	随机种子	固定随机数，让每次运行生成的数据集完全一样，结果可复现
    x, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                      cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=11)


    plt.figure()
    # x[:, 0]：取 x 的所有行、第 0 列→所有样本的第一个特征（对应坐标系 X 轴）；
    # x[:, 1]：取 x 的所有行、第 1 列→所有样本的第二个特征（对应坐标系 Y 轴）；
    # marker='o'：数据点用圆圈表示（还可以选 '+'、'*'、's' 等）；
    # 无c参数→所有点都是默认蓝色，不区分聚类；
    plt.scatter(x[:, 0], x[:, 1], marker='o')
    plt.show()

    # 3.实例化模型
    # n_clusters=2	要聚成的簇数（K 值）	强制将数据聚成2 类（哪怕数据天然是 4 类，也会按规则合并）
    # init='k-means++'	初始聚类中心的选择方式	最优选择方式：避免随机选中心导致的局部最优解，让聚类结果更稳定
    # n_init='auto'	重新初始化中心的次数	自动选择次数，多次初始化后选效果最好的结果，避免局部最优
    kmeans_cls = KMeans(n_clusters=2, init='k-means++', n_init='auto')

    # 4.模型训练
    # fit_predict(x)：KMeans 的核心方法，一次性完成训练和预测
    # fit：用特征数据x训练模型，即 KMeans 算法执行 “选中心→分簇→更新中心→重复收敛” 的过程；
    # predict：对训练数据x做聚类预测，得到每个样本的聚类标签；
    # 返回值y_pred：形状为(1000,)的一维数组，每个元素是 0 或 1（因为 n_clusters=2），表示对应样本被分到了第 0 簇或第 1 簇。
    y_pred = kmeans_cls.fit_predict(x)
    # c=y_pred：按聚类预测标签给数据点上色，不同簇的点显示不同颜色（比如 0 簇红色、1 簇蓝色）
    plt.scatter(x[:, 0], x[:, 1], c=y_pred)
    plt.show()

    # 5.模型预测
    print(calinski_harabasz_score(x, y_pred))

    # 3.实例化模型
    kmeans_cls = KMeans(n_clusters=3, init='k-means++', n_init='auto')

    # 4.模型训练
    y_pred = kmeans_cls.fit_predict(x)
    plt.scatter(x[:, 0], x[:, 1], c=y_pred)
    plt.show()

    # 5.模型预测
    print(calinski_harabasz_score(x, y_pred))

    # 3.实例化模型
    kmeans_cls = KMeans(n_clusters=4, init='k-means++', n_init='auto')

    # 4.模型训练
    y_pred = kmeans_cls.fit_predict(x)
    plt.scatter(x[:, 0], x[:, 1], c=y_pred)
    plt.show()

    # 5.模型预测
    print(calinski_harabasz_score(x, y_pred))


if __name__ == '__main__':
    dm03_kmean_demo()
