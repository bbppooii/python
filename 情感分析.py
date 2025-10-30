import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

positive_texts = [
    "I love this movie", "This was amazing", "Fantastic plot", "Very enjoyable", "Loved the acting",
    "A brilliant film", "Outstanding direction", "Great experience", "Best movie ever", "Will watch again"
]
negative_texts = [
    "I hate this film", "Worst movie", "Terrible acting", "Very boring", "I dislike it",
    "Awful experience", "Bad plot", "I regret watching", "Horrible", "Waste of time"
]

texts = positive_texts + negative_texts
labels = [1]*10 + [0]*10

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=6, padding='post')

X_train, X_test, y_train, y_test = train_test_split(padded, labels, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 16, input_length=6),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(np.array(X_train), np.array(y_train), epochs=20,
                    validation_data=(np.array(X_test), np.array(y_test)), verbose=2)

plt.figure()
plt.plot(history.history['accuracy'], label='训练准确率')
plt.plot(history.history['val_accuracy'], label='验证准确率')
plt.title("训练与验证准确率")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig("准确率曲线.png")
plt.show()

plt.figure()
plt.plot(history.history['loss'], label='训练损失')
plt.plot(history.history['val_loss'], label='验证损失')
plt.title("训练与验证损失")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.savefig("损失曲线.png")
plt.show()

df = pd.DataFrame({"text": texts, "label": labels})
df.to_csv("造的数据.csv", index=False)
