import sqlite3
con = sqlite3.connect("userdata.db")
cur = con.cursor()
cur.execute(""" INSERT INTO Employee (username, password)
                VALUES (Username, Password)
            """)
con.commit()

con = sqlite3.connect("userdata.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE user
            (
            username TEXT NOT NULL PRIMARY KEY,
            password TEXT NOT NULL
            )
        """)
