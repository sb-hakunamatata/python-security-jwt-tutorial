from random import randrange


class IOTPModel:
    def generate_otp(self, user_id: str):
        pass

    def get_otp(self, user_id: str):
        pass


# TODO: InMemory Implementation -> Database Injection.
class OTPModel(IOTPModel):
    def __init__(self):
        self.otp = {}

    def generate_otp(self, user_id: str):
        otp = randrange(10000, 99999)
        self.otp[user_id] = otp
        return otp

    def get_otp(self, user_id: str):
        return self.otp[user_id]
