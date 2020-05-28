import sqlite3
import pandas as pd

# DB 연결
conn = sqlite3.connect('./output/sample.db')

# 데이터프레임을 이용하여 테이블 정의
df = pd.DataFrame(
    [[1, 'James', 'M', 25],
     [2, 'Wendy', 'F', 22]],
    columns=['id', 'name', 'sex', 'age']
)

print(df, '\n')

ndf = df.set_index('id')
print(ndf)

# DB에 변경사항 저장
ndf.to_sql('User', conn)

# DB 연결 종료
conn.close()
