"""
Exercice de la page 77.

Enoncé:
    • Nous souhaitons avoir une application qui permet de construire des
    véhicules (Voiture, Camion), chaque véhicule est composé de
    plusieurs autres objets (moteur, roue) en fonction du type du
    véhicule.
    • En utilisant le pattern builder implémentez cette application.
"""
class Moteur:
    """
    Classe definissant un Moteur
    """
    def __init__(self, type, marque):
        self.type = type
        self.marque = marque


class Roue:
    """
    Classe definissant une Roue
    """
    def __init__(self, taille, marque):
        self.type = type
        self.marque = marque


class Vehicule:
    """
    Classe definissant un Vehicule
    """
    def __init__(self, type, marque, moteur = None, roues= []):
        self.type = type
        self.moteur = moteur
        self.roue = []
        self.marque = marque

    @property
    def nombre_roue(self):
        return len(self.roue)


class VehiculeBuilder:
    """
    Cette classe est un Builder de la classe voiture.

    Chaque methode du builder retourne un objet de la classe builder.
    """
    def __init__(self):
        self._type = ""
        self._marque = ""
        self._moteur = None
        self._roues = []

    def type(self, type):
        self._type = type
        return self

    def marque(self, marque):
        self._marque = marque
        return self

    def moteur(self, moteur):
        self._moteur = moteur
        return self

    def moteur_electrique(self, marque):
        self.moteur(Moteur("electrique", marque))
        return self

    def roue(self, *roue):
        self._roues += roue
        return self

    def type_roue(self, type_roue, nombre):
        for i in range(nombre):
            self._roues.append(Roue(type_roue, self._marque))
        return self

    def build(self):

        return Vehicule(self._type, self._marque, self._moteur, self._roues)
