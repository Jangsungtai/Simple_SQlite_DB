import streamlit as st
import pandas as pd
from db.db_operations import get_all_students, get_student_grades, add_student, delete_student, update_student_grade, add_student_grade, search_students

st.title('Student Information Management')

# 맨 상단: 전체 학생 테이블 검색
if st.checkbox('Show All Students'):
    students_df = get_all_students()
    st.dataframe(students_df, use_container_width=True, hide_index=True)

# 성적 검색 섹션 (Expander 사용)
with st.expander("Search Student Grades by ID", expanded=False):
    st.subheader('Search Student Grades')

    student_id = st.number_input("Enter Student ID", min_value=1, step=1)
    if st.button('Search Grades'):
        grades_df = get_student_grades(student_id)
        if grades_df is not None and not grades_df.empty:
            # 각 컬럼을 순서대로 표시
            for index, row in grades_df.iterrows():
                st.write(f"**Student ID**: {row['id']}")
                st.write(f"**Name**: {row['name']}")
                st.image(row['img'], caption=row['name'], width=150)
                st.write(f"**GPA**: {row['gpa']}")
                st.write(f"**Birthdate**: {row['birthdate']}")
                st.write(f"**Grade**: {row['grade']}")
                st.write(f"**Admission Date**: {row['admission_date']}")
                st.write(f"**Major**: {row['major']}")
                st.write(f"**Address**: {row['address']}")
                st.write(f"**Email**: {row['email']}")
                st.write("---")
        else:
            st.write(f"No grades found for student ID: {student_id}")

# 학생 추가 섹션
with st.expander("Add New Student", expanded=False):
    st.subheader("Add New Student")

    with st.form("add_student_form"):
        name = st.text_input("Name")
        birthdate = st.date_input("Birthdate")
        admission_date = st.date_input("Admission Date")
        grade = st.number_input("Grade", min_value=1, max_value=4)
        major = st.text_input("Major")
        address = st.text_input("Address")
        email = st.text_input("Email")
        img_path = st.text_input("Image Path (e.g., db/img/1.jpg)")

        submitted = st.form_submit_button("Add Student")
        if submitted:
            add_student(name, birthdate, admission_date, grade, major, address, email, img_path)
            st.success(f"Student {name} added successfully!")

# 학생 삭제 섹션
with st.expander("Delete Student", expanded=False):
    st.subheader("Delete Student")

    student_id_to_delete = st.number_input("Enter Student ID to Delete", min_value=1, step=1)
    if st.button('Delete Student'):
        delete_student(student_id_to_delete)
        st.success(f"Student ID {student_id_to_delete} deleted successfully!")

# 학생 성적 수정 섹션
with st.expander("Update Student Grade", expanded=False):
    st.subheader("Update Student Grade")

    student_id_to_update = st.number_input("Enter Student ID to Update", min_value=1, step=1)
    new_gpa = st.number_input("Enter New GPA", min_value=0.0, max_value=4.0, step=0.1)
    if st.button('Update Grade'):
        update_student_grade(student_id_to_update, new_gpa)
        st.success(f"Student ID {student_id_to_update}'s GPA updated to {new_gpa}!")
