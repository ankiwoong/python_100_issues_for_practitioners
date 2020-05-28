import sqlite3
import pandas as pd

# DB 연결
conn = sqlite3.connect('./output/sample.db')

# SQL 쿼리를 이용하여 데이터프레임으로 저장
sql = 'SELECT * from Product limit 3'
df = pd.read_sql_query(sql, conn)
print(df)

# DB 연결 종료
conn.close()
