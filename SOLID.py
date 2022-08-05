from abc import abstractmethod


class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Voyageur(Personne):
    def __init__(self, nom, prenom, nationalite):
        super().__init__(nom, prenom)
        self.nationalite = nationalite


class Calculatrice:

    def add(self, a, b):
        return a + b

    @abstractmethod()
    def abstract(self):
        pass


class CalculatriceNulle(Calculatrice):

    def add(self, a, b):
        raise NotImplementedError("Cette méthode n'est pas implémentée")


class Moteur:
    def __init__(self, marque):
        self.marque = marque


class VoitureNulle:
    """
    Cette voiture a un moteur deja defini.
    On ne peut pas choisir le moteur de la voiture.
    """
    def __init__(self):
        self.moteur = Moteur("Nulle")
        self.couleur = "Nulle"


class Voiture:
    """
    Ici a la créatino de la voiture je choisi le moteur.
    """
    def __init__(self, moteur, couleur):
        self.moteur = moteur
        self.couleur = couleur

moteur = Moteur("Diesel")
voiture = Voiture(moteur, "rouge")

voiture_nulle = VoitureNulle()