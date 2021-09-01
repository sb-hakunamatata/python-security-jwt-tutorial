from .config import Config


class DynamoConfig:
    DYNAMO_URL: str = "endpoint"
    DYNAMO_CONFIG: str = "DYNAMODB"
    DYNAMO_TABLE: str = "table"

    @staticmethod
    def get_dynamodb_url():
        return Config.config().get(DynamoConfig.DYNAMO_CONFIG, DynamoConfig.DYNAMO_URL)

    @staticmethod
    def get_dynamodb_table():
        return Config.config().get(DynamoConfig.DYNAMO_CONFIG, DynamoConfig.DYNAMO_TABLE)