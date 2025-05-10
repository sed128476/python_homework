import pandas as pd
import sqlite3
import os

# Create db directory if it doesn't exist
db_dir = "../db"
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Create and connect to the database
db_path = os.path.join(db_dir, "company.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Drop existing tables to recreate with new structure
cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute("DROP TABLE IF EXISTS project")

# Create project table
cursor.execute("""
CREATE TABLE IF NOT EXISTS project (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

# Create employee table with manager field
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    department_id INTEGER,
    employee_id INTEGER PRIMARY KEY,
    salary REAL NOT NULL,
    is_manager BOOLEAN DEFAULT 0,
    FOREIGN KEY (department_id) REFERENCES project (id)
)
""")

# Check if project data exists before inserting
cursor.execute("SELECT COUNT(*) FROM project")
if cursor.fetchone()[0] == 0:
    # Insert sample data into project table
    cursor.execute("""
    INSERT INTO project (name, department) VALUES
    ('Project A', 'HR'),
    ('Project B', 'IT'),
    ('Project C', 'Finance')
    """)

# Check if employee data exists before inserting
cursor.execute("SELECT COUNT(*) FROM employee")
if cursor.fetchone()[0] == 0:
    # Insert sample employee data with managers
    cursor.execute("""
    INSERT INTO employee (department_id, employee_id, salary, is_manager) VALUES
    (1, 101, 85000, 1),  -- HR Manager
    (1, 102, 55000, 0),  -- HR Employee
    (2, 201, 95000, 1),  -- IT Manager
    (2, 202, 65000, 0),  -- IT Employee
    (3, 301, 105000, 1), -- Finance Manager
    (3, 302, 75000, 0)   -- Finance Employee
    """)

# Commit the changes
conn.commit()

# Query to find departments with average salary > 70000 and their managers
high_salary_query = """
WITH department_stats AS (
    SELECT 
        p.department,
        AVG(e.salary) as avg_salary
    FROM project p
    JOIN employee e ON p.id = e.department_id
    GROUP BY p.department
    HAVING AVG(e.salary) > 70000
)
SELECT 
    p.department,
    ROUND(ds.avg_salary, 2) as average_salary,
    e.employee_id as manager_id,
    e.salary as manager_salary
FROM department_stats ds
JOIN project p ON p.department = ds.department
JOIN employee e ON e.department_id = p.id
WHERE e.is_manager = 1
ORDER BY ds.avg_salary DESC;
"""

print("\nDepartments with Average Salary > $70,000 and their Managers:")
print("Department | Average Salary | Manager ID | Manager Salary")
print("-" * 60)
cursor.execute(high_salary_query)
results = cursor.fetchall()
for row in results:
    print(f"{row[0]:<10} | ${row[1]:<14,.2f} | {row[2]:<10} | ${row[3]:,.2f}")

# Close the connection
conn.close()