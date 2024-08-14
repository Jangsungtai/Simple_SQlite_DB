import sqlite3
import os

# 데이터베이스 연결
db_path = os.path.join('data', 'students.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 상위 테이블 생성 (추가된 컬럼 포함)
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_total (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthdate TEXT,
    admission_date TEXT,
    grade INTEGER,
    major TEXT,
    address TEXT,
    email TEXT,
    img TEXT,
    gender TEXT,
    personality TEXT,
    race TEXT
)
''')

# 하부 테이블 생성 (추가된 컬럼 포함)
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    name TEXT,
    gpa REAL,
    religion TEXT,
    dominant_hand TEXT,
    FOREIGN KEY (student_id) REFERENCES student_total(id)
)
''')

# 샘플 데이터 작성 (총 25개)
import random

names = [
    'John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis',
    'Diana Evans', 'Edward Harris', 'Fiona Green', 'George Hall', 'Hannah King',
    'Ivy Lewis', 'Jack Miller', 'Katie Nelson', 'Leo O’Brien', 'Mia Parker',
    'Nathan Quinn', 'Olivia Reed', 'Paul Scott', 'Quincy Turner', 'Rachel Underwood',
    'Sam Vincent', 'Tina Wilson', 'Uma Xavier', 'Victor Young', 'Wendy Zimmerman'
]

personalities = ['Friendly', 'Shy', 'Outgoing', 'Calm', 'Energetic', 'Serious']
races = ['black', 'white', 'yellow']
religions = ['Christian', 'Muslim', 'Jewish', 'Buddhist', 'Hindu', 'Atheist']
hands = ['left', 'right']

sample_students = []
sample_grades = []

for i in range(25):
    name = names[i]
    birthdate = f"{random.randint(1995, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    admission_date = f"{random.randint(2015, 2021)}-09-01"
    grade = random.randint(1, 4)
    major = random.choice(['Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Economics', 'Engineering'])
    address = f"{random.randint(100, 999)} Main St"
    email = f"{name.split()[0].lower()}@example.com"
    img = f"db/img/{i+1}.jpg"
    gender = random.choice(['m', 'f'])
    personality = random.choice(personalities)
    race = random.choice(races)

    student = (name, birthdate, admission_date, grade, major, address, email, img, gender, personality, race)
    sample_students.append(student)

    gpa = round(random.uniform(50, 100), 2)
    religion = random.choice(religions)
    dominant_hand = random.choice(hands)

    grade_entry = (i+1, name, gpa, religion, dominant_hand)
    sample_grades.append(grade_entry)

# 데이터 삽입
cursor.executemany('''
INSERT INTO student_total (name, birthdate, admission_date, grade, major, address, email, img, gender, personality, race)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', sample_students)

cursor.executemany('''
INSERT INTO student_grades (student_id, name, gpa, religion, dominant_hand)
VALUES (?, ?, ?, ?, ?)
''', sample_grades)

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()
