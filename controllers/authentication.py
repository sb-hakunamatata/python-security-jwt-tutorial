from flask_classful import FlaskView as FlaskController, route, request
from models import IAuthenticationModel
from http import HTTPStatus


class AuthenticationController(FlaskController):
    authModel: IAuthenticationModel = None

    @classmethod
    def initialize(cls, authModel: IAuthenticationModel):
        AuthenticationController.authModel = authModel

    @route('/auth/<user_id>/otp/generate', methods=['POST'])
    def generate_otp(self, user_id: str):
        return {
            "otp": self.authModel.generate_pass(user_id)
        }

    @route('/auth/<user_id>/otp/<int:otp>/login', methods=['POST'])
    def login(self, user_id: str, otp: int):
        if not self.authModel.verify_pass(user_id, otp):
            return "UnAuthorized", HTTPStatus.UNAUTHORIZED.value
        return {
            "token": self.authModel.generate_token(user_id)
        }

    @classmethod
    def get_token(cls, token: str):
        if token.startswith("Bearer "):
            return token.replace("Bearer ", "")
        return token

    @route('/auth/get_user', methods=['GET'])
    def get_user_id(self):
        auth_header = request.headers['Authorization']
        if not auth_header:
            return 'UnAuthorized', HTTPStatus.UNAUTHORIZED.value
        user_id = self.authModel.verify_token(token=self.get_token(token=auth_header))
        if user_id is None:
            return 'UnAuthorized', HTTPStatus.UNAUTHORIZED.value
        return {
            "user_id": user_id
        }