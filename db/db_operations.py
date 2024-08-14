import sqlite3
import pandas as pd

# 데이터베이스 연결 함수
def connect_db():
    return sqlite3.connect('data/students.db')

# 모든 학생 정보 가져오기 (지정된 컬럼만 선택)
def get_all_students():
    conn = connect_db()
    query = '''
    SELECT *
    FROM student_total
    ORDER BY id ASC
    '''
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 학생 성적 조회 (지정된 컬럼만 선택, 이미지 없을 시 기본 이미지 설정)
def get_student_grades(student_id):
    conn = connect_db()
    query = '''
    SELECT student_total.id, student_total.name, student_total.img, student_grades.gpa,
           student_total.birthdate, student_total.grade, student_total.admission_date,
           student_total.major, student_total.address, student_total.email,
           student_grades.religion, student_grades.dominant_hand
    FROM student_total
    LEFT JOIN student_grades ON student_total.id = student_grades.student_id
    WHERE student_total.id = ?
    '''
    df = pd.read_sql(query, conn, params=(student_id,))
    
    # 이미지가 없을 경우 기본 이미지 설정
    df['img'] = df['img'].apply(lambda x: x if x else 'db/12.jpg')
    
    conn.close()
    return df

# 새로운 학생 추가 (초기 성적 정보도 추가)
def add_student(name, birthdate, admission_date, grade, major, address, email, img):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO student_total (name, birthdate, admission_date, grade, major, address, email, img)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, birthdate, admission_date, grade, major, address, email, img))
    
    student_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO student_grades (student_id, name, gpa, religion, dominant_hand)
    VALUES (?, ?, ?, ?, ?)
    ''', (student_id, name, 0.0, 'Unknown', 'right'))  # 초기 성적 정보 추가 (GPA 0.0, religion, dominant_hand 기본값)
    
    conn.commit()
    conn.close()

# 학생 삭제
def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM student_total WHERE id = ?', (student_id,))
    cursor.execute('DELETE FROM student_grades WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()

# 학생 성적 수정
def update_student_grade(student_id, new_gpa):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE student_grades SET gpa = ? WHERE student_id = ?
    ''', (new_gpa, student_id))
    conn.commit()
    conn.close()

def add_student_grade(student_id, name, gpa):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO student_grades (student_id, name, gpa)
    VALUES (?, ?, ?)
    ''', (student_id, name, gpa))
    conn.commit()
    conn.close()

def search_students(query_condition):
    conn = connect_db()
    query = f"SELECT * FROM student_grades WHERE {query_condition}"
    try:
        df = pd.read_sql(query, conn)
    except Exception as e:
        df = None
        print(f"Error executing query: {e}")
    conn.close()
    return df

# 전공별 집계 함수
def get_major_aggregates(major):
    conn = connect_db()

    if major == "ALL":
        query = '''
        SELECT
            COUNT(*) AS total_students,
            AVG(CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER)) AS average_age,
            SUM(CASE WHEN gender = 'm' THEN 1 ELSE 0 END) AS male_students,
            SUM(CASE WHEN gender = 'f' THEN 1 ELSE 0 END) AS female_students,
            AVG(gpa) AS average_gpa
        FROM student_total
        LEFT JOIN student_grades ON student_total.id = student_grades.student_id
        '''
        df = pd.read_sql(query, conn)
    else:
        query = '''
        SELECT
            COUNT(*) AS total_students,
            AVG(CAST((julianday('now') - julianday(birthdate)) / 365.25 AS INTEGER)) AS average_age,
            SUM(CASE WHEN gender = 'm' THEN 1 ELSE 0 END) AS male_students,
            SUM(CASE WHEN gender = 'f' THEN 1 ELSE 0 END) AS female_students,
            AVG(gpa) AS average_gpa
        FROM student_total
        LEFT JOIN student_grades ON student_total.id = student_grades.student_id
        WHERE major = ?
        '''
        df = pd.read_sql(query, conn, params=(major,))

    conn.close()
    return df
