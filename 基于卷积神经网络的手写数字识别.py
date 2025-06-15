import tensorflow as tf
from tensorflow.keras import layers, models

# 1. 加载 MNIST 数据
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# 归一化并增加通道维度
x_train = x_train[..., None] / 255.0
x_test  = x_test [..., None] / 255.0

# 2. 构建简单 CNN
model = models.Sequential([
    layers.Conv2D(32, kernel_size=3, activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(pool_size=2),
    layers.Conv2D(64, kernel_size=3, activation='relu'),
    layers.MaxPooling2D(pool_size=2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 3. 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# 4. 训练
model.fit(x_train, y_train,
          epochs=5,
          batch_size=128,
          validation_split=0.1)

# 5. 评估
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"测试集准确率：{test_acc:.3f}")
