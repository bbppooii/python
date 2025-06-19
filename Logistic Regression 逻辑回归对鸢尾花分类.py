import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score

# 1. 读取数据
df = pd.read_csv('iris.arff.csv')  # 如果在其他路径请替换为完整路径

# 2. 标签编码：将 'class' 列转为数值型
df['class_id'] = LabelEncoder().fit_transform(df['class'])

# 3. 特征与标签
X = df[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']].values
y = df['class_id'].values

# 4. 划分训练/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# 5. 训练逻辑回归模型
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 6. 预测并评估准确率
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"逻辑回归分类准确率：{acc:.3f}")

# 7. PCA降维（用于二维可视化）
pca = PCA(n_components=2)
X_all = np.vstack([X_train, X_test])
X_pca = pca.fit_transform(X_all)
train_pca = X_pca[:len(X_train)]
test_pca = X_pca[len(X_train):]

# 8. 绘制分类结果图
plt.figure(figsize=(6,6), dpi=80)
plt.scatter(train_pca[:, 0], train_pca[:, 1], c=y_train, marker='o', edgecolors='k', label='Train')
plt.scatter(test_pca[:, 0], test_pca[:, 1], c=y_pred, marker='x', label='Test Pred')
plt.legend()
plt.title(f'Logistic Regression on Iris\nAccuracy: {acc:.3f}')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.tight_layout()
plt.show()
