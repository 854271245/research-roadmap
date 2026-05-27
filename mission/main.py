import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("data.csv")

# 查看数据
print(df)

# 检查缺失值
print("\n缺失值：")
print(df.isnull().sum())
print("\n平均销量：")
print(df["sales"].mean())

print("\n最大销量：")
print(df["sales"].max())

if (df["inventory"] < 200).any():
    print("建议补货")
if ((df["sales"] < 100) & (df["inventory"] > 250)).any():
    print("建议促销")

plt.scatter(df["price"], df["sales"])

plt.xlabel("Price")
plt.ylabel("Sales")
plt.title("Price vs Sales")


plt.show()

plt.scatter(df["ad_cost"], df["sales"])

plt.xlabel("Ad Cost")
plt.ylabel("Sales")
plt.title("Ad Cost vs Sales")

plt.show()

# 画销量图
plt.plot(df["sales"])

plt.title("Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.show()