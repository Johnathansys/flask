from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name")
    if name == None:
        return render_template("index.html")
    else:
        return "Greetings, " + name, "!"