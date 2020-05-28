import sqlite3

# DB 연결 (DB가 없는 경우, 새로운 DB 파일 생성)
conn = sqlite3.connect('./output/sample.db')
print(conn)

# Connection 객체에서 Cursor 생성
cur = conn.cursor()
print(cur)

# DB 연결 종료
conn.close()
