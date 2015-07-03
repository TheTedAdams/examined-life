from flask import Flask
from flask_restful import Api
from .resources.oauth2 import Oauth2

app = Flask(__name__)
api = Api(app)
api.add_resource(Oauth2, '/oauth2')
