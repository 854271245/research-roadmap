import pandas as pd

data = {
    "name": ["Alic", "Bb", "Cidy", "Dvid"],
    "math": [40, 78, 85, 55],
    "english": [85, 80, 92, 89]
}

df = pd.DataFrame(data)

print(df)

print("\n平均数学成绩：")
print(df["math"].mean())

print("\n最高英语成绩：")
print(df["english"].max())