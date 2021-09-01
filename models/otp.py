from random import randrange
import hashlib
from dao import IOTPDao

class IOTPModel:
    def generate_otp(self, user_id: str):
        pass

    def validate_otp(self, user_id: str, otp: int):
        pass


def get_otp_digest(otp: int):
    return hashlib.md5(str(otp).encode()).hexdigest()


class OTPModel(IOTPModel):
    def __init__(self, otpDAO: IOTPDao):
        self.otpDAO = otpDAO

    def generate_otp(self, user_id: str):
        otp = randrange(10000, 99999)
        self.otpDAO.save_otp(user_id, get_otp_digest(otp=otp))
        return otp

    def validate_otp(self, user_id: str, otp: int):
        return self.otpDAO.retrieve_otp(user_id=user_id) == get_otp_digest(otp=otp)
