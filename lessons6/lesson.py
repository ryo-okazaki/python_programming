"""
[DEFAULT]
debug = False

[web_server]


"""

import configparser

# configファイル書き込み

# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': 'True'
# }
# config['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
# config['db_server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)


# configファイル読み込み
config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])