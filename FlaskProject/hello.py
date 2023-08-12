from flask import Flask
# Set in Flask to set FLASK_app = hello.py
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

print(__name__)
if __name__ =="__main__":
    app.run()