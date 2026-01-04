import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 读取数据
df = pd.read_csv("jena_climate_2009_2016.csv")
df = df[5::6]  # 每小时一条，原始数据每10分钟一条

# 选取温度作为目标
temp = df["T (degC)"].values

# 标准化
mean = temp[:200000].mean()
std = temp[:200000].std()
temp = (temp - mean) / std

# 构建数据集
past = 24 * 5  # 使用过去5天（即120小时）作为输入
future = 24    # 预测24小时后的温度
step = 1

def create_dataset(data, past, future, step):
    X, y = [], []
    for i in range(past, len(data) - future):
        X.append(data[i - past:i:step])
        y.append(data[i + future])
    return np.array(X), np.array(y)

X, y = create_dataset(temp, past, future, step)
X = X[..., np.newaxis]  # 添加特征维度

# 划分训练测试集
split = int(0.8 * len(X))
X_train, y_train = X[:split], y[:split]
X_test, y_test = X[split:], y[split:]

# 建立模型
model = Sequential([
    LSTM(64, input_shape=X_train.shape[1:]),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10, batch_size=128, validation_split=0.2)

# 评估
loss = model.evaluate(X_test, y_test)
print(f"测试损失（均方误差）：{loss:.4f}")

# 预测示例
pred = model.predict(X_test[:100])
plt.figure(figsize=(10, 4))
plt.plot(pred, label='Predicted')
plt.plot(y_test[:100], label='Actual')
plt.legend()
plt.title("未来24小时温度预测")
plt.show()

