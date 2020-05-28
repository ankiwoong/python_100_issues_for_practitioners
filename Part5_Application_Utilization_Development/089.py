import sqlite3

# DB 연결
conn = sqlite3.connect('./output/sample.db')
cur = conn.cursor()

# Product 테이블의 id=1인 행 레코드의 가격을 7000원으로 수정
cur.execute('UPDATE Product set title="새 제품", price=7000 where id=1')
conn.commit()

# 변경 내용 확인
cur.execute('SELECT * from Product where id=1')
rows = cur.fetchall()
for row in rows:
    print(row)

# DB 연결 종료
conn.close()
