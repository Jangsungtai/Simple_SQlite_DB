1. 실행 with streamlit
2. 실행화면 
1) 메인화면 
![image](https://github.com/user-attachments/assets/fc0db39e-50fb-4d2f-bf40-423b80caa743 width="150" height="150")
2) 전체 데이터검색 
![image](https://github.com/user-attachments/assets/3571af70-739c-4455-9551-888f3ff4e20a width="150" height="150")
3) 개벌 레코드 접근 (SELECT 명령어) 
![image](https://github.com/user-attachments/assets/2705c4aa-6484-48ed-a7d2-bc380e8a8ff1 width="150" height="150")
4) 집계함수 (SUM, AVG, COUNT)
![image](https://github.com/user-attachments/assets/b6f9e395-ae36-4deb-8e0b-fcb649caadc9 width="150" height="150")

2. 폴더 
  C:\Code work\DB_edu\
  │
  ├── app.py               # Streamlit 애플리케이션의 진입점
  
  ├── db\
  
  │   ├── __init__.py      # 빈 파일
  
  │   └── db_operations.py # 데이터베이스 연산(조회, 입력 등)을 처리하는 파일
  
  │   └── img\             # 이미지 폴더 
  
  ├── data\
  
  │   ├── init_db.py       # SQLite 데이터베이스 초기화 및 샘플 데이터 삽입
  
  │   └── students.db      # SQLite 데이터베이스 파일
  
  └── requirements.txt     # 필요한 패키지 목록


3. 구현 기능 
  1. init : 테이블 두개 생성
   1) 테이블1 : 학생 10명 공개 가능 자료, 이미지 
   2) 테이블2 : 성적 저장 
  
  2. 실행 : STREAMLIT 구현 
   1) 테이블1 검색 
   2) 테이블2 검색 (이미지 처리)
   3) 학생추가
   4) 학생삭제
   5) 학생성적수정 




