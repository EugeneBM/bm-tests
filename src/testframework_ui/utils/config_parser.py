import configparser
import os


class ConfigParser:
    config = None
    abs_path = os.path.abspath("test_settings.cfg")

    @staticmethod
    def get_settings():
        if ConfigParser.config is None:
            ConfigParser.config = configparser.RawConfigParser()
            ConfigParser.config.read(ConfigParser.abs_path)

        return ConfigParser.config
