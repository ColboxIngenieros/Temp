from importlib import resources
import json

def cfg_item(*items):
    data = Config.get_instance().data
    for key in items:
        data = data[key]
    return data

class Config:

    __instance = None

    @staticmethod
    def get_instance(): #funcion de acceso a la instancia 
        if Config.__instance is None:
            Config()
        return Config.__instance
    
    def __init__(self): #nos aseguramos que solo haya una instancia de Config
        if Config.__instance is None:
            Config.__instance = self

            file_path = resources.files("falling_letters.assets.config").joinpath('config.json')
            with resources.as_file(file_path) as config_data_path:
                with open(config_data_path) as file:
                    self.data = json.load(file)
        else:
            raise Exception("There can be only one Config!!")