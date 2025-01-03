from flask import Flask

def create_app():
    app = Flask('website')

    #config 
    #security key, test mode, debugging window 

    #blueprints
    from app.index.routes import index
    app.register_blueprint(index)

    return app