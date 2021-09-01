from .otp import IOTPDao
from .otp import OTPDao
from configuration import DynamoConfig

OTPDao = OTPDao(DynamoConfig.get_dynamodb_url(), DynamoConfig.get_dynamodb_table())