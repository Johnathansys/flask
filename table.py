import sqlite3
con = sqlite.connect("database.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE Employee
            (
            EmpID INTEGER NOT NULL PRIMARY KEY,
            EMPName VARCHAR(20) NOT NULL,
            HireDate DATE,
            Salary CURRENCY
            )
        """)