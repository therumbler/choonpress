import configparser

def get_config():
    filepath = 'choonpress/etc/config.conf'
    cp = configparser.ConfigParser()
    with open(filepath) as f:
        cp.readfp(f)

    config = {}
    for section in cp.sections():
        items = cp.items(section)
        config[section] = {item[0]: item[1] for item in items}

    return config

