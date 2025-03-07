import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE Student
            (
            StudentID VARCHAR(6) PRIMARY KEY,
            Surname VARCHAR(20) NOT NULL,
            FirstName VARCHAR(15),
            DateOfBirth DATE
            )
        """)