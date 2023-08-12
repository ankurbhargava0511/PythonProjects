from flask import Flask
# Set in Flask to set FLASK_app = hello.py
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye bye changed<p>"

@app.route("/<name>")
def name_hello(name):
    return f"hello {name}"


if __name__ =="__main__":
    app.run(debug=True)