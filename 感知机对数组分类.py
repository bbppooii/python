import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# 1. 构造样本数据
X = np.array([
    [2, 1],
    [1, -1],
    [-1, -1],
    [-2, 1]
])
# y: 对应标签 +1 或 -1
y = np.array([1, 1, -1, -1])

# 2. 初始化并训练感知机
clf = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
clf.fit(X, y)

# 3. 预测
y_pred = clf.predict(X)

# 4. 准确率
print("预测标签：", y_pred)
print("训练准确率：", accuracy_score(y, y_pred))

# 5. 如果有新样本，也可直接 predict
new_samples = np.array([[0, 0], [3, 2], [-3, -2]])
print("新样本预测：", clf.predict(new_samples))
