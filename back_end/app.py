#flask run statement: flask --app app run

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_test():
    return "<p>Test</p>" 
