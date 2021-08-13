from flask import Flask
from .authentication import AuthenticationController
from models import AuthenticationModel

app: Flask = Flask(__name__)

# register our controller here.
AuthenticationController.initialize(AuthenticationModel)
AuthenticationController.register(app, route_base="/")