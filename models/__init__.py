from .authentication import IAuthenticationModel
from .authentication import AuthenticationModel
from .otp import OTPModel


OTPModel = OTPModel()
AuthenticationModel = AuthenticationModel(OTPModel)