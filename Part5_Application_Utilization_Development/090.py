import sqlite3

# DB 연결
conn = sqlite3.connect('./output/sample.db')
cur = conn.cursor()

# Product 테이블의 id=1인 행 레코드를 삭제
cur.execute('DELETE from Product where id=1')
conn.commit()

# 변경 내용 확인
cur.execute('SELECT * from Product')
rows = cur.fetchall()
for row in rows:
    print(row)

# DB 연결 종료
conn.close()
