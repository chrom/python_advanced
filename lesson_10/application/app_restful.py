from flask import Flask
from flask_restful import Api
from .resources import UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/user', '/user/<string:id>')