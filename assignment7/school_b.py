import sqlite3 

# Connect to the database

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Alice', 20, 'Computer Science')  
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")

# Fetch and print student data
cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")
result = cursor.fetchall()
for row in result:
    print(row)  # Removed the extra parenthesis


def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # Ensure tuple format with comma
    results = cursor.fetchall()
    
    if results:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    
    if results:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return
    
    try:
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    except sqlite3.IntegrityError:
        print(f"{student} is already enrolled in {course}.")

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key constraint
    cursor = conn.cursor()

    # Enroll students in courses
    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")

    conn.commit()  # Commit transactions
    print("Student enrollments completed successfully.")

   # cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (95, 43))



#cursor.execute("INSERT INTO Enrollments (student_id, course_id) (95, 43)")

def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()

    if results:  # Check if results exist
        print(f"Student {student} is already enrolled in course {course}.")
        return  # Now it's inside the function and valid

    
#    cursor.execute("SELECT * FROM Enrollments ")
#    result = cursor.fetchall()
#for row in result:
#    print(row)  # Removed the extra parenthesis


    # Fetch all table names
#    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#    tables = cursor.fetchall()

    # Print the table names
#    for table in tables:
#        print("table" ,table[0])  # Extract just the table name
