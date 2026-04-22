import pandas as pd
from sqlalchemy import create_engine,text

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

insert_sql = text("INSERT INTO students(name,dob,mark,group_id) values('Tien Anh','2010-09-19',8,1)")
#conn = engine.connect()
with engine.connect() as conn:
    conn.excute(insert_sql)
    conn.commit()


# DB có bảng users(id,name,email,salary)
# yêu cầu:
# 1. Tao 1 file users.csv có 20 người theo thông tin trên
# 2. Nạp dữ liệu vào db- table: users
# 3. THêm 1 column: net_salary
# 4. Tính dữ liệu vào net_salary (giar sử net = salary-10%)
# 5. Xuất dữ liệu mới ra csv
