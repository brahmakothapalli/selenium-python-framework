import configparser
import sys

config = configparser.RawConfigParser()
print('Sys Path : ', sys.path[0])
# config.read(sys.path[0] + "\\pytest.ini")
config.read("/home/brahma/python_works/selenium-python-framework/pytest.ini")


class ReadConfiguration:

    @staticmethod
    def get_url():
        return config.get('config data', 'base_url')

    @staticmethod
    def get_username():
        return config.get('config data', 'user_name')

    @staticmethod
    def get_password():
        return config.get('config data', 'password')
