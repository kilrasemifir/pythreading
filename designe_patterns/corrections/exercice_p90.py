"""
Exercice de la page 90.

Enoncé:
    • Nous souhaitons créer un jeu de papier pierre ciseaux en utilisant un
    modèle de stratégie.
    • Vous pouvez sélectionner n'importe quelle stratégie parmi pierre,
    papier, ciseaux et une stratégie au hasard pour l’ordinateur.
    • Implémentez le jeu.
"""
import random


class JeuPPC:
    """
    Jeu du pierre papier ciseaux.
    """
    def __init__(self, strategy):
        self.strategy = strategy

    def jouer(self, coup):
        """
        Joue un coup.
        """
        ordinateur = self.strategy.choisir_coup()
        if coup == ordinateur:
            print("Egalité")
        elif coup == "pierre" and ordinateur == "ciseaux":
            print("Vous avez gagné")
        elif coup == "ciseaux" and ordinateur == "papier":
            print("Vous avez gagné")
        elif coup == "papier" and ordinateur == "pierre":
            print("Vous avez gagné")
        else:
            print("Vous avez perdu")


class StrategieAleatoire:
    """
    Stratégie aléatoire.
    """
    def choisir_coup(self):
        """
        Choisit un coup aléatoire.
        """
        return random.choice(["pierre", "papier", "ciseaux"])


class StrategieStatique:
    """
    Stratégie de papier.
    """
    def __init__(self, coup):
        self.coup = coup
    def choisir_coup(self):
        """
        Choisit le coup papier.
        """
        return self.coup


if __name__ == "__main__":
    jeu = JeuPPC(StrategieStatique("papier"))
    fini = False
    while not fini:
        coup = input("Entrez votre coup: ")
        if coup == "fin":
            fini = True
        elif coup not in ["pierre", "papier", "ciseaux"]:
            print("Coup invalide")
        else:
            jeu.jouer(coup)