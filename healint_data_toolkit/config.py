import logging
import os
from typing import Dict

import toml

from healint_data_toolkit.exceptions import InvalidConfigFormatError
from healint_data_toolkit.models.config import *
from healint_data_toolkit.constants import ConfigKey


class ConfigManager:

    """
        automatically construct config object for various purposes

        requires the config file to have a standardized structure
    """

    def __init__(self, config_path: str):

        with open(config_path, "r") as file:
            self.parsed_object = toml.loads(file.read())

        self._db_config = {}

    @property
    def db_config(self) -> Dict[str, "DatabaseConfig"]:

        if not self._db_config:
            self._db_config = self._construct_db_config()

        return self._db_config

    def _construct_db_config(self) -> Dict[str, "DatabaseConfig"]:
        if ConfigKey.DATABASE.value not in self.parsed_object:
            raise InvalidConfigFormatError

        database_object = self.parsed_object[ConfigKey.DATABASE.value]

        db_config = {}

        for credential_name, credential_info in database_object.items():
            DatabaseConfig(**credential_info)
            db_config[credential_name] = DatabaseConfig(**credential_info)

        logging.warning(f"{len(db_config)} db credentials parsed. ")

        return db_config

    @staticmethod
    def init_temp_folder():
        """
        init a temp folder in the project root
        :return:
        """
        # init temp folder
        if not os.path.exists("temp"):
            os.mkdir("temp")
            logging.warning("**temp** folder is created at project root.")
