from .config import Config
import os


class AuthenticationConfig:
    AUTH_SECRET: str = "auth_secret"
    AUTH_ALGO: str = "auth_algo"
    AUTHENTICATION: str = "AUTHENTICATION"

    @staticmethod
    def get_auth_secret():
        return Config.config().get(AuthenticationConfig.AUTHENTICATION, AuthenticationConfig.AUTH_SECRET,
                                   vars=os.environ)

    @staticmethod
    def get_auth_algo():
        return Config.config().get(AuthenticationConfig.AUTHENTICATION, AuthenticationConfig.AUTH_ALGO)
