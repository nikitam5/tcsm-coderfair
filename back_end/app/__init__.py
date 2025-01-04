from flask import Flask
from .routes import init_routes

def create_app():
    app = Flask('website')

    #config 
    #security key, test mode, debugging window 

    #blueprints
    from app.index.routes import index
    app.register_blueprint(index)

    # Register the routes by calling init_routes
    init_routes(app)

    return app