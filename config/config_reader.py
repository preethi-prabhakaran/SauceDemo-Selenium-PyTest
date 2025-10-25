import os
import yaml

def read_config():
    with open("config/config.yaml", 'r') as f:
        return yaml.safe_load(f)

config_data = read_config()
# config.yaml is maintained for a fallback mechanism, in case environment variable is not set. config_reader reads the yaml file and gets the required values

def base_url():
    return os.getenv("BASE_URL", config_data['base_url'])

def headless():
    return os.getenv("HEADLESS", config_data['headless'])

def valid_creds():
    return config_data['credentials']['valid_user']['username'], config_data['credentials']['valid_user']['password']

def invalid_creds():
    return config_data['credentials']['invalid_user']['username'], config_data['credentials']['invalid_user']['password']

def product1_name():
    return os.getenv("PRODUCT1", config_data['product1'])

def product2_name():
    return os.getenv("PRODUCT2", config_data['product2'])

def first_name():
    return os.getenv("FIRST_NAME", config_data['first_name'])

def last_name():
    return os.getenv("LAST_NAME", config_data['last_name'])

def postal_code():
    return os.getenv("POSTAL_CODE", config_data['postal_code'])