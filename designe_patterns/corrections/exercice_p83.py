"""
Exercice de la page 83.

Enoncé:
    • Créer un singleton thread safe pour extraire des informations de
    configuration à partir d’un fichier.
"""
from threading import Lock
import json

class ConfigThreadSafe:
    """
    Classe singleton
    """
    _instance = None
    __lock = Lock()

    def __init__(self):
        self.file_path = "config.json"
        self.config = {}
        self.load_config()

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def load_config(self):
        with open(self.file_path, "r") as f:
            self.config = json.load(f)

    def __repr__(self):
        return str(self.config)


if __name__ == "__main__":
    config = ConfigThreadSafe()
    print(config)
    config2 = ConfigThreadSafe()
    print(config2)
    print(config is config2)