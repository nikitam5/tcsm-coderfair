from flask import Flask, Blueprint

index = Blueprint('index', 'index')

@index.route('/')
def test():
    return "<p>index</p>"