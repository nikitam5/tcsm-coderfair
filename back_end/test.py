from flask import Flask

app = Flask("Test")
@app.route("/")
def hello_test():
    return "<p>Hello</p>"
