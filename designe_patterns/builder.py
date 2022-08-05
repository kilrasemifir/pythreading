class Voiture:
    def __init__(self,
                 marque,
                 couleur,
                 moteur,
                 nombre_porte,
                 km,
                 prix):
        self.marque = marque
        self.couleur = couleur
        self.moteur = moteur
        self.nombre_porte = nombre_porte
        self.km = km
        self.prix = prix


class VehiculeBuilder:
    def __init__(self):
        self._marque = ""
        self._couleur = ""
        self._moteur = ""
        self._nombre_porte = 0
        self._km = 0
        self._prix = 0
        self._type = "Voiture"

    def type(self, type):
        self._type = type
        return self

    def marque(self, marque):
        self.marque = marque
        return self

    def couleur(self, couleur):
        self.couleur = couleur
        return self

    def moteur(self, moteur):
        self.moteur = moteur
        return self

    def nombre_porte(self, nombre_porte):
        self.nombre_porte = nombre_porte
        return self

    def km(self, km):
        self.km = km
        return self

    def prix(self, prix):
        self.prix = prix
        return self

    def build(self):
        if self._type == "Voiture":
            return Voiture(self._marque,
                           self._couleur,
                           self._moteur,
                           self._nombre_porte,
                           self._km,
                           self._prix)


voiture =VehiculeBuilder()\
           .marque("Renault")\
           .couleur("rouge")\
           .moteur("Diesel")\
           .prix(10000)\
           .build()