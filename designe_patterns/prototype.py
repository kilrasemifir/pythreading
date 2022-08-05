"""
Exemple d'utilisation d'un design pattern Prototype.

Le design pattern Prototype permet de créer des objets qui sont "copiés"
"""


class Moto:
    def __init__(self, moteur, couleur):
        self.couleur = couleur
        self.moteur = moteur


class Voiture:
    def __init__(self, moteur, couleur):
        self.couleur = couleur
        self.moteur = moteur


class Camion:
    def __init__(self, moteur, couleur):
        self.couleur = couleur
        self.moteur = moteur


class Moteur:
    def __init__(self, marque):
        self.marque = marque


def vehicule_prototype(type):
    if type == "Voiture":
        return Voiture(Moteur("Diesel"), "rouge")
    if type == "Moto":
        return Moto(Moteur("Diesel"), "rouge")
    if type == "Camion":
        return Camion(Moteur("Diesel"), "rouge")