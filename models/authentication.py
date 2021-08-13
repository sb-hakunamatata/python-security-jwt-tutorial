from .otp import IOTPModel
import jwt
from jwt import InvalidSignatureError
from configuration import AuthenticationConfig


class IAuthenticationModel:
    def generate_pass(self, user_id: str):
        pass

    def verify_pass(self, user_id: str, otp: int):
        pass

    def generate_token(self, user_id: str):
        pass

    def verify_token(self, token: str):
        pass


# SOLID principal
class AuthenticationModel(IAuthenticationModel):
    def __init__(self, otpModel: IOTPModel):
        self.otpModel = otpModel

    def generate_pass(self, user_id: str):
        return self.otpModel.generate_otp(user_id)

    def verify_pass(self, user_id: str, otp: int):
        return self.otpModel.get_otp(user_id) == otp

    def generate_token(self, user_id: str):
        return jwt.encode({
            "signature": "AuthenticationSuccess",
            "user_id": user_id,
        }, key=AuthenticationConfig.get_auth_secret(), algorithm=AuthenticationConfig.get_auth_algo())

    def verify_token(self, token: str):
        try:
            decoded_token = jwt.decode(token, AuthenticationConfig.get_auth_secret(),
                                       AuthenticationConfig.get_auth_algo())
            if decoded_token["signature"] != "AuthenticationSuccess":
                return None
            else:
                return decoded_token["user_id"]
        except InvalidSignatureError:
            return None
