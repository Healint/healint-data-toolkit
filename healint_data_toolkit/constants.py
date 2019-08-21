from enum import Enum


class ConfigKey(Enum):
    CORE = "core"
    DATABASE = "database"


class HTTPRequestPageSourceOutput(Enum):
    FILE = "FILE"
    STRING = "STRING"
    SOUP = "SOUP"
    JSON = "JSON"
