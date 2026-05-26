import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["Alice", "Bob", "Cindy", "David", "Eva"],
    "math": [90, 78, 88, 95, 70],
    "english": [85, 80, 92, 89, 75],
    "physics":[80,95,85,64,100]
}

df = pd.DataFrame(data)

print("学生成绩表：")
print(df)

# 新增总分列
df["total"] = df["math"] + df["english"] + df["physics"]

print("\n总分：")
print(df)

# 平均成绩
print("\n数学平均分：")
print(df["math"].mean())

print("\n英语平均分：")
print(df["english"].mean())

print("物理平均分：")
print(df["physics"].mean())
# 找最高分
top_student = df.loc[df["total"].idxmax()]

print("\n总分最高学生：")
print(top_student)

# 画图
plt.bar(df["name"], df["total"])

plt.xlabel("Student")
plt.ylabel("Total Score")
plt.title("Student Total Scores")

plt.show()