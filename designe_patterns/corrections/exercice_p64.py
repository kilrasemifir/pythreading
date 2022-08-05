"""
Exercice de la page 64.

Enoncé:
    Nous souhaitons créer une application qui permet fabriquer différents
    types de cafés, chaque café à un cout et un nom:
        • Colombia, Expresso, Deca,…
    • L’application permet d’ajouter différents ingrédients à votre café,
    chaque ingrédient a un cout également
    • Sirop de vanille, chocolat, lait, noisette,…
    • Modélisez et implémentez cette application en utilisant le pattern
    décorateur.
"""


class Cafe:
    """
    Classe de base. Il représente le café de base.
    """
    def __init__(self, nom, cout):
        self._nom = nom
        self.cout = cout

    def __str__(self):
        return "{} : {}".format(self.nom, self.cout)

    @property
    def prix(self):
        return self.cout

    @property
    def nom(self):
        return self._nom


class IngredientDecorateur:
    """
    On utilise le decorateur pour ajouter un ingrédient à un café.
    """
    def __init__(self, base, nom, cout):
        self.base = base
        self._nom = nom
        self.cout = cout

    def __str__(self):
        return "{} : {}".format(self.nom, self.cout)

    @property
    def prix(self):
        return self.cout + self.base.prix

    @property
    def nom(self):
        return f"{self.base.nom} ,{self._nom}"


if __name__ == "__main__":
    type_cafe = {
        "colombia": Cafe("Colombia", 2),
        "expresso": Cafe("Expresso", 1),
        "deca": Cafe("Deca", 2),
        "cappuccino": Cafe("Cappuccino", 1.5),
        "macchiato": Cafe("Macchiato", 3),
        "mocha": Cafe("Mocha", 3),
        "americano": Cafe("Americano", 3.5),
    }
    type_incredients = {
        "Sucre": 0,
        "Chocolat": 1,
        "Lait": 0.5,
        "Noisette": 0.5,
        "Vanille": 0.5,
    }
    print("Quel type de café voulez-vous ? Nous pouvons vous proposer: ")
    for key in type_cafe:
        print(f"    {type_cafe[key]} €")
    print("?")

    while (type := input("Entrez le type de café: ")) not in type_cafe:
        print("Nous n'avons pas ce type de café, veuillez recommencer.")
    cafe = type_cafe[type]

    print("Choix des ingrédients:")
    for ingredient in type_incredients:
        if input(f"Voulez vous un {ingredient} pour +{type_incredients[ingredient]} €? (y/n)").lower() == "y":
            cafe = IngredientDecorateur(cafe, ingredient, type_incredients[ingredient])

    print(f"""
Vous avez choisi le café {cafe.nom}
prix total : {cafe.prix} €
""")