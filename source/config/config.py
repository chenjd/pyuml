import configparser
import os
import sys

CONFIG_FILE_NAME = 'userConfig.ini'


class Config:

    def __init__(self):
        root_dir = os.path.dirname(sys.argv[0])
        self._path = os.path.join(root_dir, './config')
        self._author, self._version, self._url = self._get_config()

    @property
    def author(self):
        return self._author

    @property
    def version(self):
        return self._version

    @property
    def url(self):
        return self._url

    @staticmethod
    def _create_default_config(config_file_path):
        config_parser = configparser.ConfigParser()
        config_parser['DEFAULT'] = {'Author': 'jiadong chen & liam',
                                    'Version': '0.0.1',
                                    'Url': 'https://github.com/chenjd/pyuml'}
        with open(config_file_path, 'w') as configfile:
            config_parser.write(configfile)

        return config_parser['DEFAULT']['Author'], config_parser['DEFAULT'][
            'Version'], config_parser['DEFAULT']['Url']

    def _get_config(self):
        if not os.path.exists(self._path):
            os.mkdir(self._path)
        config_file_path = os.path.join(self._path, CONFIG_FILE_NAME)
        if not os.path.exists(config_file_path):
            return self._create_default_config(config_file_path)
        else:
            config_parser = configparser.ConfigParser()
            config_parser.read(config_file_path)
        return config_parser['DEFAULT']['Author'], config_parser['DEFAULT'][
            'Version'], config_parser['DEFAULT']['Url']
