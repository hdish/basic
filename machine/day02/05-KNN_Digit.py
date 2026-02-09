import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

import warnings
warnings.filterwarnings('ignore')

#2.读取数据并展示数据
#2.1读取数据
data = pd.read_csv('手写数字识别.csv')
x = data.iloc[:, 1:]
y = data.iloc[:, 0]
# print(Counter(y))

#2.2展示数据
digit = x.iloc[1000].values
img = digit.reshape(28, 28)
plt.imshow(img)
plt.imsave('demo.png', img)
plt.show()


