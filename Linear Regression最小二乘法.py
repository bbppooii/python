import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 读取数据（假设 boston.csv 与脚本位于同一目录）
df = pd.read_csv('boston.csv')

# 2. 准备特征矩阵 X 和目标向量 y
#    假设最后一列 'medv' 为房价目标
X = df.iloc[:, df.columns != 'medv'].values
y = df['medv'].values

# 3. 划分训练/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# 4. 训练最小二乘线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 5. 在测试集上预测并评估
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)
print(f"测试集 MSE: {mse:.3f}")
print(f"测试集 R² : {r2:.3f}")

# 6. 可视化：实际值 vs 预测值
plt.figure(figsize=(6,6), dpi=80)
plt.scatter(y_test, y_pred, edgecolors='k', alpha=0.7)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--', linewidth=2
)
plt.xlabel('Actual Price (medv)')
plt.ylabel('Predicted Price')
plt.title('Linear Regression: Actual vs Predicted')
plt.tight_layout()
plt.show()
