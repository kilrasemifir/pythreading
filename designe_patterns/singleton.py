class Singleton:
    """
    Classe singleton
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    singleton = Singleton()
    print(singleton)
    singleton2 = Singleton()
    print(singleton2)
    print(singleton is singleton2)