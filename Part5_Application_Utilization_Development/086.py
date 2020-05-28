import sqlite3

# DB 연결
conn = sqlite3.connect('./output/sample.db')
cur = conn.cursor()

# Cursor를 통해, SQL 쿼리 실행
sql = '''
CREATE TABLE Product (
id integer primary key autoincrement,
title text not null,
price integer,
link text)
'''

cur.execute(sql)

# DB 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
