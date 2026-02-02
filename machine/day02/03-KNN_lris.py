from sklearn.datasets import load_iris

# 导入数据
iris_data = load_iris()

print(f'{iris_data.data[:5]}')
print(f'{iris_data.target}')
print(f'{iris_data.target_names}')
print(f'{iris_data.feature_names}')
