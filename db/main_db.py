import sqlite3
from config import path_db
from db import queries

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.students_table)
    conn.commit()
    conn.close()

def add_student(name, age, grade):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_student, (name, age, grade))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return student_id

def update_student_grade(student_id, new_grade):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_student, (new_grade, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_student, (student_id,))
    conn.commit()
    conn.close()