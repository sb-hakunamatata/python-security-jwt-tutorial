import configparser


class Config:
    __conf: configparser.ConfigParser = None

    @staticmethod
    def init_config(config_path: str):
        if Config.__conf is None:
            Config.__conf = configparser.ConfigParser()
            Config.__conf.read(config_path)
        return Config.__conf

    @staticmethod
    def config():
        return Config.__conf