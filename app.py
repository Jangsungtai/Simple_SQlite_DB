import streamlit as st
import pandas as pd
from db.db_operations import get_all_students, get_student_grades, add_student, delete_student, update_student_grade, get_major_aggregates, add_student_grade, search_students

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
                st.write(f"**Religion**: {row['religion']}")
                st.write(f"**Dominant Hand**: {row['dominant_hand']}")
                st.write("---")
        else:
            st.write(f"No grades found for student ID: {student_id}")


# 전공 그룹별 집계 섹션 (Expander 사용)
with st.expander("Aggregate Functions by Major Group", expanded=False):
    st.subheader('Aggregate Functions by Major Group')

    # 전공 그룹 선택 (ALL 옵션 추가)
    major_group = st.selectbox("Select Major Group", ["ALL", "Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "History", "Literature", "Economics", "Engineering"])

    if st.button('Get Aggregates'):
        aggregates_df = get_major_aggregates(major_group)
        if aggregates_df is not None and not aggregates_df.empty:
            total_students = aggregates_df.loc[0, 'total_students']
            average_age = aggregates_df.loc[0, 'average_age']
            male_students = aggregates_df.loc[0, 'male_students']
            female_students = aggregates_df.loc[0, 'female_students']
            average_gpa = aggregates_df.loc[0, 'average_gpa']

            # None 타입에 대한 처리를 추가
            st.write(f"**Total Students**: {total_students if total_students is not None else 'N/A'}")
            st.write(f"**Average Age**: {average_age:.1f}" if average_age is not None else "**Average Age**: N/A")
            st.write(f"**Male Students**: {male_students if male_students is not None else 'N/A'}")
            st.write(f"**Female Students**: {female_students if female_students is not None else 'N/A'}")
            st.write(f"**Average GPA**: {average_gpa:.2f}" if average_gpa is not None else "**Average GPA**: N/A")
        else:
            st.write(f"No data found for major group: {major_group}")

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
