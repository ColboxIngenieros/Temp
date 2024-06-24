import json
from importlib import resources

def cfg(*items):
    d = Config.get_instance().data
    for k in items:
        d = d[k]
    return d
    

class Config:

    __config_json_path = ["marquee.assets.config","config.json"]

    #configuracion singelton
    __instance = None

    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config()

        return Config.__instance

    def __init__(self):
        if Config.__instance is None:
            Config.__instance = self

            file_path = resources.files(Config.__config_json_path[0]).joinpath(Config.__config_json_path[1])
            with resources.as_file(file_path) as json_path:
                with open(json_path) as file:
                    self.data = json.load(file)
        else:
            raise Exception("Config doesn´t allow multiple instances")