import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# 1. 加载数据
df = pd.read_csv('loans.csv')  # 注意：根据实际路径调整文件名

# 2. 编码分类变量
df_encoded = df.copy()
label_cols = ['grade', 'sub_grade', 'home_ownership', 'purpose', 'term']
for col in label_cols:
    df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

# 3. 特征和标签
X = df_encoded.drop(columns=['safe_loans'])
y = df_encoded['safe_loans'].apply(lambda x: 1 if x == 1 else 0)  # 转换为 0 和 1

# 4. 拆分训练和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. 构建决策树（使用 ID3 算法 = 信息增益）
clf = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# 6. 可视化决策树
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=["High Risk", "Safe"], filled=True, rounded=True)
plt.show()
