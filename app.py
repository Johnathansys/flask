from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    username = request.args.get("username")
    if username == None:
        return render_template("index.html")
    elif username == "John":
        return "Hello, John :D"
    else:
        return "user not recognised >:[ "
    
    