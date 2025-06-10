import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score

# 1. 加载数据
df = pd.read_csv('iris.arff.csv')

# 2. 数值化类别标签
df['class_id'] = df['class'].astype('category').cat.codes

# 3. 仅用前三个特征
X = df[['sepallength','sepalwidth','petallength']].values
y = df['class_id'].values

# 4. 划分训练/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# 5. 训练 KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 6. 测试及准确率
y_pred = knn.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"KNN (first 3 features) — Test accuracy: {acc:.3f}")

# 7. PCA 降到 2D 用于可视化
pca = PCA(n_components=2)
X_all_red = pca.fit_transform(np.vstack([X_train, X_test]))
train_red = X_all_red[:len(X_train)]
test_red  = X_all_red[len(X_train):]

# 8. 绘图
plt.figure(figsize=(6,5), dpi=80)
plt.scatter(train_red[:,0], train_red[:,1],
            c=y_train, marker='o', edgecolors='k', label='train')
plt.scatter(test_red[:,0], test_red[:,1],
            c=y_pred, marker='x', label='test_pred')
plt.legend()
plt.title("KNN on Iris (first 3 features)\nPCA 2D projection")
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
