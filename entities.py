from universal_globals import *


class Entity:
    def __init__(self, name, *args, **kwargs):
        pass


class Experimental_Entity:
    def __init__(self, *args, **kwargs):
        for dictionary in args:
            for key in dictionary:
                if type(key) == "dict":
                    for attr in key:
                        setattr(self, attr, key[attr])
            else:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

        defaults = {
            "hp": 100,
        }
        for key in defaults:
            setattr(self, key, defaults[key])
        
        essentials = ["name", "hp"]
        for i in essentials:
            if not i in self.__dict__:
                print(f"missing value '{i}' in 'Object'")
                # raise MissingValueError(f"missing value \'{i}\' in \'Object\'")


