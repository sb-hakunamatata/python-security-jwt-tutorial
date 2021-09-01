import boto3


class IOTPDao:
    def save_otp(self, user_id: str, otp: str):
        pass

    def retrieve_otp(self, user_id: str):
        pass


class OTPDao(IOTPDao):
    def __init__(self, dynamoURL: str, tableName: str):
        self.conn = boto3.resource('dynamodb', endpoint_url=dynamoURL).Table(tableName)

    def save_otp(self, user_id: str, otp: str):
        self.conn.put_item(Item={
            'otp': otp,
            'user': user_id,
        })

    def retrieve_otp(self, user_id: str):
        return self.conn.get_item(Key={
            'user': user_id
        })['Item']['otp']
