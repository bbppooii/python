import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. 读取数据
df = pd.read_csv('order.csv')  # 请根据你的实际路径调整文件名

# 2. 选择用于聚类的特征列
features = ['total_items', 'discount%', 'weekday', 'hour',
            'Food%', 'Fresh%', 'Drinks%', 'Home%', 'Beauty%',
            'Health%', 'Baby%', 'Pets%']
X = df[features]

# 3. 标准化数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. KMeans 聚类（这里设置为3类，可以根据需求改为其他数字）
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 5. 使用 PCA 将数据降维为2D 用于可视化
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 6. 可视化聚类结果
plt.figure(figsize=(8,6), dpi=100)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], cmap='viridis', edgecolors='k')
plt.title('K-means')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.grid(True)
plt.tight_layout()
plt.show()
