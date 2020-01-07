from flask import Flask, request
import requests


from application.blueprints.users import users
from application.blueprints.publics import publics

    
def create_app():

    app = Flask(__name__)

    app.register_blueprint(users)
    app.register_blueprint(publics)


    return app