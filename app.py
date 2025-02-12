from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        Username = request.form["Username"]
        Password = request.form["Password"]
        if Password == "123":
            return "Greetings, " + Username + "!"
        else:
            return "Wrong Password :P "