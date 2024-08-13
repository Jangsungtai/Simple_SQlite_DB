import sqlite3
import os

# 데이터베이스 연결
db_path = os.path.join('data', 'students.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 상위 테이블 생성 (img 컬럼 포함)
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
    img TEXT
)
''')

# 샘플 이미지 경로 설정
img_folder = os.path.join('db', 'img')
sample_images = [os.path.join(img_folder, f'{i}.jpg') for i in range(1, 11)]

# 샘플 데이터 삽입 (상위 테이블)
sample_students = [
    ('John Doe', '2000-01-01', '2018-09-01', 4, 'Computer Science', '123 Main St', 'john@example.com', sample_images[0]),
    ('Jane Smith', '2001-02-02', '2019-09-01', 3, 'Mathematics', '456 Elm St', 'jane@example.com', sample_images[1]),
    ('Alice Johnson', '1999-03-15', '2017-09-01', 4, 'Physics', '789 Maple St', 'alice@example.com', sample_images[2]),
    ('Bob Brown', '2002-04-20', '2020-09-01', 2, 'Chemistry', '321 Oak St', 'bob@example.com', sample_images[3]),
    ('Charlie Davis', '2001-05-25', '2019-09-01', 3, 'Biology', '654 Pine St', 'charlie@example.com', sample_images[4]),
    ('Diana Evans', '2000-06-30', '2018-09-01', 4, 'History', '987 Cedar St', 'diana@example.com', sample_images[5]),
    ('Edward Harris', '2003-07-15', '2021-09-01', 1, 'Mathematics', '123 Birch St', 'edward@example.com', sample_images[6]),
    ('Fiona Green', '2001-08-10', '2019-09-01', 3, 'Literature', '456 Walnut St', 'fiona@example.com', sample_images[7]),
    ('George Hall', '2000-09-05', '2018-09-01', 4, 'Economics', '789 Poplar St', 'george@example.com', sample_images[8]),
    ('Hannah King', '1999-10-20', '2017-09-01', 4, 'Engineering', '321 Elm St', 'hannah@example.com', sample_images[9])
]

cursor.executemany('''
INSERT INTO student_total (name, birthdate, admission_date, grade, major, address, email, img)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', sample_students)

# 하부 테이블 생성 (학생별 테이블)
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    name TEXT,
    gpa REAL,
    FOREIGN KEY (student_id) REFERENCES student_total(id)
)
''')

# 샘플 데이터 삽입 (하부 테이블)
sample_grades = [
    (1, 'John Doe', 3.8),
    (2, 'Jane Smith', 3.6),
    (3, 'Alice Johnson', 3.9),
    (4, 'Bob Brown', 3.2),
    (5, 'Charlie Davis', 3.4),
    (6, 'Diana Evans', 3.7),
    (7, 'Edward Harris', 3.5),
    (8, 'Fiona Green', 3.6),
    (9, 'George Hall', 3.9),
    (10, 'Hannah King', 3.8)
]

cursor.executemany('''
INSERT INTO student_grades (student_id, name, gpa)
VALUES (?, ?, ?)
''', sample_grades)

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()
