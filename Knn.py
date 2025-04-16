import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
wine = load_wine()
print("数据集的键：", wine.keys())
print("\n数据集描述：\n", wine.DESCR)
print("\n特征数据的维度：", wine.data.shape)    # (178, 13)
print("目标数据的维度：", wine.target.shape)      # (178,)
print("特征名称：", wine.feature_names)

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target,
                                                    test_size=0.3, random_state=42)
print("\n训练集特征数据的维度：", X_train.shape)
print("训练集目标数据的维度：", y_train.shape)
print("测试集特征数据的维度：", X_test.shape)
print("测试集目标数据的维度：", y_test.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
train_score = knn.score(X_train, y_train)
print("\n训练集准确率：", train_score)

new_sample = X_train[0] + np.random.normal(0, 0.1, size=X_train.shape[1])
new_sample = new_sample.reshape(1, -1)
new_pred = knn.predict(new_sample)
print("新样本预测的类别：", new_pred)

test_score = knn.score(X_test, y_test)
print("测试集准确率：", test_score)

labels = ['Train Accuracy', 'Test Accuracy']
scores = [train_score, test_score]

plt.figure(figsize=(6, 4))
plt.bar(labels, scores, color=['blue', 'green'])
plt.ylim([0, 1])
plt.title('KNN 分类准确率')
plt.ylabel('准确率')
for i, score in enumerate(scores):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=12)

plt.show()
