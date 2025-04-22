import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier

X, y = make_blobs(n_samples=300, centers=2, random_state=42, cluster_std=2.0)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k', s=50)
plt.title("生成的数据集")
plt.xlabel("特征1")
plt.ylabel("特征2")
plt.show()

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k', s=50)
plt.title("KNN 分类边界")
plt.xlabel("特征1")
plt.ylabel("特征2")
plt.show()

new_points = np.array([[0, 0], [5, 5], [-5, 5]])
new_preds = knn.predict(new_points)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k', s=50)

for i, (pt, pred) in enumerate(zip(new_points, new_preds)):
    plt.scatter(pt[0], pt[1], marker='p', s=200, edgecolor='k',
                facecolor='yellow')

plt.title("新数据分类预测")
plt.xlabel("特征1")
plt.ylabel("特征2")
plt.show()
