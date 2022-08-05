"""
Exemple de design pattern Singleton.

Un singleton
"""


class Singleton:
    """
    Un singleton est une classe qui ne peut etre instancier qu'une seule fois.
    """
    __instance = None # L'unique instance de notre classe
    __count = 0 # Compteur du nombre d'instances

    def __init__(self):
        self.value = 0
        Singleton.__count += 1
        if Singleton.__instance:
            raise Exception("This class is a singleton")

    @classmethod
    def get_instance(cls):
        """
        Methode qui permet d'obtenir l'unique instance de notre classe.
        :return:
        """
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    def __str__(self):
        return "Singleton "+ str(Singleton.__count)

    def increment(self):
        """
        Exemple de methode de la classe singleton.
        Elle incremente la valeur de l'unique instance.
        :return: rien
        """
        self.value += 1


singleton = Singleton.get_instance()
singleton.increment()
singleton2 = Singleton.get_instance()
singleton2.increment()

print(singleton, singleton2, singleton.value, singleton2.value)