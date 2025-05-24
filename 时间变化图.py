import random
import time

import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体
mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号

x = range(1, 101)
times = [random.randint(10, 200) for i in range(100)]
plt.figure(figsize=(15, 5), dpi=80)  # 创建画布
plt.plot(x, times, color='r', linestyle='-', label='t = 2', marker='v')  # 绘制折线图，点划线

plt.legend(loc=0)  # 显示图例
# 描述信息
plt.xlabel("设备数/个")
plt.ylabel("时间/s")
plt.title("时间变化图", fontsize=18)

plt.savefig("./time.jpg")  # 保存至指定位置
plt.show()  # 显示图像