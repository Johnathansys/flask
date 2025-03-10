import sqlite3
con = sqlite3.connect("userdata.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE user
            (
            username TEXT NOT NULL PRIMARY KEY,
            password TEXT NOT NULL 
            )
        """)