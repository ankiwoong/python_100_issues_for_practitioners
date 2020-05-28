import sqlite3
import pandas as pd

# DB 연결
conn = sqlite3.connect('./output/sample.db')

# SQL 쿼리를 이용하여 데이터프레임으로 저장
sql = 'SELECT * from User'
df = pd.read_sql_query(sql, conn, index_col='id')
print(df, '\n')

# 행 추가
df.loc[3] = ('Adam', 'M', 30)
print(df)

# DB에 변경사항 저장
df.to_sql('User', conn, if_exists='replace')

# DB 연결 종료
conn.close()
