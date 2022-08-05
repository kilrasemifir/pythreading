"""
Proxy design pattern.

Permet de créer une classe qui effectue une logique a l'appel d'une methode de la classe cible.
"""

class Maison:
    """
    Classe cible de notre design pattern.
    """
    def __init__(self, adresse):
        self.adresse = adresse

    def entrer(self):
        print("Entrer dans la maison a l'adresse {}".format(self.adresse))


class Alarme:
    """
    Proxy design pattern.
    Affiche un message quand on entre dans la maison.s
    """
    def __init__(self, maison):
        self.maison = maison
        self.foo = lambda : 0

    def subscribe(self, foo):
        self.foo = foo

    def entrer(self):
        self.foo()
        self.maison.entrer()

ma_maison = Maison("rue de la paix")
ma_maison = Alarme(ma_maison)
ma_maison.subscribe(lambda : print("Alarme sonore"))
ma_maison.entrer()
