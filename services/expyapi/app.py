from flask import Flask
from flask_restful import Api
from .resources.oauth2 import Oauth2
from .resources.users import UserList, User
from .resources.entities import EntityList, Entity

app = Flask(__name__)
api = Api(app)

api.add_resource(Oauth2, '/oauth2')
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')
api.add_resource(EntityList, '/entities')
api.add_resource(Entity, '/entities/<entity_id>')
