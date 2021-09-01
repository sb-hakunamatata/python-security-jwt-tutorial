from .authentication import IAuthenticationModel
from .authentication import AuthenticationModel
from .otp import OTPModel
from .user import UserModel
from .user import IUserModel
from dao import OTPDao

OTPModel = OTPModel(OTPDao)
UserModel = UserModel()
AuthenticationModel = AuthenticationModel(OTPModel)