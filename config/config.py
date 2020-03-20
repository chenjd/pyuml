import configparser
import os

CONFIG_FILE_NAME = './config/userConfig.ini'


class Config:

    def __init__(self):
        self._author, self._version, self._url = self._get_config()

    def _create_default_config(self):
        config_parser = configparser.ConfigParser()
        config_parser['DEFAULT'] = {'Author': 'jiadong chen & liam',
                                   'Version': '0.0.1',
                                   'Url': 'https://github.com/chenjd/pyuml'}
        with open(CONFIG_FILE_NAME, 'w') as configfile:
            config_parser.write(configfile)

        return config_parser['DEFAULT']['Author'], config_parser['DEFAULT']['Version'], config_parser['DEFAULT']['Url']

    def _get_config(self):
        if not os.path.exists(os.path.join(os.getcwd(), CONFIG_FILE_NAME)):
            return self._create_default_config()
        else:
            config_parser = configparser.ConfigParser()
            config_parser.read(CONFIG_FILE_NAME)
        return config_parser['DEFAULT']['Author'], config_parser['DEFAULT']['Version'], config_parser['DEFAULT']['Url']
