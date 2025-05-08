import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

y = 5 * (x ** 2) + 6

df = pd.DataFrame({
    'x': x,
    'y': y
})
print("生成的数据表：")
print(df)

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = $y = 5x^2 + 6$')

plt.title('函数曲线：$y = 5x^2 + 6$')
plt.xlabel('横坐标 x')
plt.ylabel('纵坐标 y')
plt.legend()
plt.grid(True)

plt.show()
