from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("userdata.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS User
            (
            username VARCHAR(20) NOT NULL PRIMARY KEY,
            password VARCHAR(20) NOT NULL
            )
        """)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        con = sqlite3.connect("userdata.db")
        cur = con.cursor()
        cur.execute("INSERT INTO User (username, password) VALUES (?, ?)",
                        (request.form["Username"], request.form["Password"]))
        con.commit()
        con.close()
    return "Signup Sucessful"
    
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        Username = request.form["Username"]
        Password = request.form["Password"]
        if Password == "123" and Username == "Bob":
            return "Hello" + Username
        else:
            return "Login Failed"