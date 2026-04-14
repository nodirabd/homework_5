students_table = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
"""

insert_student = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)"

select_students = "SELECT * FROM students"

update_student = "UPDATE students SET grade = ? WHERE id = ?"

delete_student = "DELETE FROM students WHERE id = ?"