
import configparser

config_name = 'config.ini'

def load_config():
    config = configparser.ConfigParser()
    config.read(config_name)
    print("all is ", config.defaults())
    return (config.defaults())
    print("all is ", config.sections())
    return config.sections()

def save_config():
    config = configparser.ConfigParser()
    config["DEFAULT"] = {
        'auto': 'False',
        'erase': 'False',
        'advanced': 'False',
    }

    with open(config_name, 'w') as file:
        config.write(file)

def get_confg_dict():
    config = load_config()
    if len(config) is 0:
        save_config()
        config = load_config()
    return config

if __name__ == '__main__':
    config = get_confg_dict()
    print(config['auto'] == 'False')
