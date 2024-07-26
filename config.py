import os
import json


CONFIG_FILE = 'config.json'

def save_config(dsn, uid, pwd, table):
    config = {
        'dsn': dsn,
        'uid': uid,
        'pwd': pwd,
        'table':table
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def load_config():
    if os.path.exists(CONFIG_FILE) and os.path.getsize(CONFIG_FILE) > 0:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {'dsn': '', 'uid': '', 'pwd': '', 'table': ''}