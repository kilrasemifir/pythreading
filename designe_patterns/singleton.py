class Singleton:
    __instance = None
    __count = 0

    def __init__(self):
        self.value = 0
        Singleton.__count += 1
        if Singleton.__instance:
            raise Exception("This class is a singleton")

    @classmethod
    def get_instance(cls):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    def __str__(self):
        return "Singleton "+ str(Singleton.__count)

    def increment(self):
        self.value += 1


singleton = Singleton.get_instance()
singleton.increment()
singleton2 = Singleton.get_instance()
singleton2.increment()

print(singleton, singleton2, singleton.value, singleton2.value)