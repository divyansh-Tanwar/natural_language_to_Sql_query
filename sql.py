import sqlite3

#connect to sqlite database
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
table_info = '''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    Class TEXT,
    section TEXT
)'''

cursor.execute(table_info)

#insert data into the table
students = ['''insert into students (name, age, grade, Class, section) values ('Alice', 14, '9th', 'A', '1')''',
            '''insert into students (name, age, grade, Class, section) values ('Bob', 15, '10th', 'B', '2')''',
            '''insert into students (name, age, grade, Class, section) values ('Charlie', 13, '8th', 'A', '1')''',
            '''insert into students (name, age, grade, Class, section) values ('David   ', 14, '9th', 'C', '3')''',
            '''insert into students (name, age, grade, Class, section) values ('Eva', 15, '10th', 'B', '2')''']

for student in students:
    cursor.execute(student)
conn.commit()
