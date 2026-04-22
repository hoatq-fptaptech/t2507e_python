import pandas as pd

df = pd.read_csv("students.csv")
# df : DataFrame (giong 1 table trong SQL)
print(df)
print(df["name"][0])
# sua diem thi cho ai duoi 25 tuoi
df.loc[df["age"]<25, "mark"] = df["mark"]+1

new_df = pd.DataFrame([
    {"name":"Quoc","age":23,"mark":8},
    {"name":"Kiet","age":18,"mark":6},
    {"name":"Dat","age":28,"mark":7}
])
df = pd.concat([df,new_df],ignore_index=True)
# luu lai vao file
df.to_csv("students.csv",index=False)

# Xay dung file du lieu san pham
# ID name, price, description image, category, qty
# tim nhung san pham qty = 0
# nhung san pham price > 1000000
# ghi file moi sau khi loc du lieu 