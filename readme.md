1. 실행 with streamlit
   
  ![image](https://github.com/user-attachments/assets/a90a296d-1457-45b6-a8d0-2841d855c914)

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




