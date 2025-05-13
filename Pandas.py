import pandas as pd
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '孙七'],
    '年龄': [25, 30, 28, 35, 22],
    '年薪': [80000, 120000, 100000, 150000, 70000]
}
df = pd.DataFrame(data)
print(df)
df_csv = pd.read_csv('员工信息.csv')
print(df_csv)
print(df_csv.head())
