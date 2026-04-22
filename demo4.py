import pandas as pd
from sqlalchemy import create_engine

db="mysql+pymysql://root:root@localhost:3306/t2507e_jp"
engine = create_engine(db)

query = "SELECT * FROM students"
df = pd.read_sql(query,engine)

print(df)

df.to_csv("students.csv",index=False)

df2 = pd.read_csv("schools.csv")
df2.to_sql(
    name="schools",
    con= engine,
    if_exists="replace", #append
    index=False
)