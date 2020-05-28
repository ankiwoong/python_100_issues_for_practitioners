import sqlite3

# DB 연결
conn = sqlite3.connect('./output/sample.db')
cur = conn.cursor()

# 방법 1 - 각 행의 레코드를 SQL 쿼리에 직접 입력
sqls = [
    '''
INSERT INTO Product (id, title, price, link)
VALUES (1, '제품 1', 1000, '/product1.html')
''',

    '''
INSERT INTO Product (id, title, price, link)
VALUES (2, '제품 2', 5000, '/product2.html')
''',

]

for sql in sqls:
    cur.execute(sql)


# 방법 2 - ? Placeholder를 활용
sql = '''
INSERT INTO Product (title, price, link) VALUES (?, ?, ?)
'''

cur.execute(sql, ('제품 3', 3000, '/product3.html'))


# 방법 3 - executemany 메소드로 여러 개의 행 레코드를 입력
sql_m = '''
INSERT INTO Product (title, price, link) VALUES (?, ?, ?)
'''

records = (
    ('제품 4', 2000, '/product4.html'),
    ('제품 5', 2000, '/product5.html'),
)

cur.executemany(sql_m, records)

# DB 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
