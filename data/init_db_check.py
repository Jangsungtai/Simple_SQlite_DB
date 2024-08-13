import sqlite3
import os 

# 데이터베이스 연결
db_path = os.path.join('data', 'students.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 테이블 목록 확인
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Existing tables:", tables)

conn.close()
