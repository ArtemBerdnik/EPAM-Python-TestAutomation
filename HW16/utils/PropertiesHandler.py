import configparser


def get_properties(value: str) -> str:
    config = configparser.RawConfigParser()
    config.read('../properties.ini')
    return config['DEFAULT'][value]


class PropertiesHandler:
    pass
