import psycopg2
from psycopg2 import sql

# Step 1: Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname='company',
    user='f_katar',
    password='f_katar34',
    host='localhost',
    port='5432'
)

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create tables using SQL commands
cursor.execute('''
CREATE TABLE IF NOT EXISTS worker (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    age INTEGER,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS department (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS project (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    worker_id INTEGER,
    FOREIGN KEY (worker_id) REFERENCES worker(id)
)
''')

# Step 4: Insert data into tables
cursor.execute("INSERT INTO department (name) VALUES ('Human Resources')")
cursor.execute("INSERT INTO worker (name, age, department_id) VALUES ('Alice', 30, 1)")

# Step 5: Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()