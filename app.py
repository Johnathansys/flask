from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    username = request.args.get("username")
    Password = request.args.get("Password")
    if Password == None:
        return render_template("index.html")
    elif Password == "123":
        return "Hello, John :D"
    else:
        return "Wrong Password :P "
    
