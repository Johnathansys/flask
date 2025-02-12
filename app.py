from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    Username = request.args.get("Username")
    Password = request.args.get("Password")
    if Password == None:
        return render_template("index.html")
    elif Password == "123":
        return "Greetings, " + Username + "!"
    else:
        return "Wrong Password :P "