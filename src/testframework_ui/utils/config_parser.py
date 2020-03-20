import configparser


class ConfigParser:
    __config_file_path = r"D:\!BmTests\bm-tests\tests\ui\test_settings.cfg"
    config = None

    @staticmethod
    def get_settings():
        if ConfigParser.config is None:
            ConfigParser.config = configparser.RawConfigParser()
            ConfigParser.config.read(ConfigParser.__config_file_path)

        return ConfigParser.config
