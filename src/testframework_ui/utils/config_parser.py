import configparser


class ConfigParser:

    __config_file_path = r"D:\!BmTests\bm-tests\tests\ui\test_settings.cfg"
    config = None

    @property
    def settings(self):
        if self.config is None:
            config = configparser.RawConfigParser()
            config.read(self.__config_file_path)

        return config