from flask import Flask
from .authentication import AuthenticationController
from models import AuthenticationModel
from models import UserModel

app: Flask = Flask(__name__)

# register our controller here.
AuthenticationController.initialize(AuthenticationModel, UserModel)
AuthenticationController.register(app, route_base="/")