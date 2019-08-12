from enum import Enum


class ConfigKey(Enum):
    CORE = 'core'
    DATABASE = 'database'


class HTTPRequestPageSourceOutput(Enum):
    FILE = 'file'
    STRING = 'string'
