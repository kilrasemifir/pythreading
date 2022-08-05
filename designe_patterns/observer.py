"""
Observer pattern

Permet de créer un object qui peut être observé par d'autres objets.
"""

from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class MaisonSubject(Subject):
    """
    Classe cible de notre design pattern.
    """

    def __init__(self):
        self.observers = []
        self.state = None

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.state)

    def entrer(self):
        self.state = "j'entre dans la maison"
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, state):
        pass


class AlarmeObserver(Observer):
    """
    Observer qui sera executé quand l'on entre dans la maison.
    """

    def update(self, state):
        print("MaisonObserver: " + state)


class SmsObserver(Observer):
    """
    Observer qui sera executé quand l'on entre dans la maison.
    """
    def update(self, state):
        print("SmsObserver: " + state)


ma_maison = MaisonSubject()
ma_maison.attach(AlarmeObserver())
ma_maison.attach(SmsObserver())
ma_maison.entrer()