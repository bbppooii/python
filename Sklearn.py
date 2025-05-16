import pandas as pd

file_path = r"C:\Users\31173\Desktop\python\dataset\boston.csv"
boston_df = pd.read_csv(file_path)

print("数据集结构信息：")
print(boston_df.info())

print("\n数据集维度：", boston_df.shape)

print("\n数据表前5行：")
print(boston_df.head())

print("\n特征名称：", list(boston_df.columns))
