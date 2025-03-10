import sqlite3 
con = sqlite3.connect("database.db") 
cur = con.cursor() 
cur.execute("""
            ALTER TABLE Student
            ADD YearsGroup INT
        """)