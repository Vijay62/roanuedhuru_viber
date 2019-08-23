import configparser
config = configparser.ConfigParser()
config.read("/root/roanuedhuru_viber/utils/settings.cnf")
username= config.get("configuration","user")
paswd= config.get("configuration","password")
auth_token= config.get("configuration","auth_token")
avatar= config.get("configuration","avatar")
name= config.get("configuration","name")