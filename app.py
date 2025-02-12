from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        Username = request.args.form["Username"]
        Password = request.args.form["Password"]
        if Password == "123":
            return "Greetings, " + Username + "!"
        else:
            return "Wrong Password :P "