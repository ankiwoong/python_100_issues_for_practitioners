import sqlite3

# DB 연결
conn = sqlite3.connect('./output/sample.db')
cur = conn.cursor()

# 방법 1 - 모든 행 레코드를 가져올 때
cur.execute('SELECT * from Product')
rows = cur.fetchall()
for row in rows:
    print(row)
print('\n')


# 방법 2 - where 조건문
cur.execute('SELECT * from Product where price=2000')
rows = cur.fetchall()
for row in rows:
    print(row)
print('\n')


# 방법 3 - where 조건문과 ? Placeholder를 활용
cur.execute('SELECT * from Product where id=? and price=?', (5, 2000))
rows = cur.fetchall()
for row in rows:
    print(row)


# DB 연결 종료
conn.close()
