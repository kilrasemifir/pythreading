from abc import abstractmethod


class Voiture:
    """
    Ici a la créatino de la voiture je choisi le moteur.
    """
    def __init__(self, moteur, couleur):
        self.moteur = moteur
        self.couleur = couleur

class Moteur:
    def __init__(self, marque):
        self.marque = marque

class Moto:
    def __init__(self, moteur, couleur):
        self.couleur = couleur
        self.moteur = moteur

class Camion:
    def __init__(self, moteur, couleur):
        self.couleur = couleur
        self.moteur = moteur


class Velo:
    def __init__(self, couleur):
        self.couleur = couleur


class VehiculeFactory:
    @abstractmethod
    def create(nombre_de_passager, volume_de_transport, couleur):
        if nombre_de_passager == 1 and volume_de_transport < 100:
            return Moto(Moteur("Diesel"), couleur)
        if volume_de_transport < 1000:
            return Voiture(Moteur("Diesel"), couleur)
        else:
            return Camion(Moteur("Diesel"), couleur)


def create(nombre_de_passager, volume_de_transport, couleur):
    if nombre_de_passager == 1 and volume_de_transport < 100:
        return Moto(Moteur("Diesel"), couleur)
    if volume_de_transport < 1000:
        return Voiture(Moteur("Diesel"), couleur)
    else:
        return Camion(Moteur("Diesel"), couleur)


print(VehiculeFactory.create(1, 10000, "rouge"))