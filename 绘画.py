import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# 加载图像
def load_image(url, image_size=(256, 256)):
    img = Image.open(BytesIO(requests.get(url).content)).convert('RGB')
    img = img.resize(image_size)
    img = np.array(img) / 255.0
    img = img[np.newaxis, ...]
    return tf.constant(img, dtype=tf.float32)

# 图像 URL
content_url = 'https://upload.wikimedia.org/wikipedia/commons/6/69/June_odd-eyed-cat.jpg'
style_url = 'https://upload.wikimedia.org/wikipedia/commons/e/ea/The_Starry_Night.JPG'

content_image = load_image(content_url)
style_image = load_image(style_url)

# 加载预训练模型
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# 风格迁移
stylized_image = hub_model(content_image, style_image)[0]

# 显示结果
plt.subplot(1, 3, 1)
plt.title("Content")
plt.imshow(content_image[0])
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Style")
plt.imshow(style_image[0])
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Stylized")
plt.imshow(stylized_image[0])
plt.axis('off')

plt.show()
