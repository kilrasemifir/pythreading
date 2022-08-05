"""
Exercice de la page 74.

Enoncé:
    • Nous souhaitons mettre en place une application qui permet de
    commander plusieurs type pizza en fonction d’un menu.
    • Chaque pizza passe par les étapes suivantes : préparer, cuire, couper
    et emballer.
    • L’application doit nous permettre d’ajouter facilement d’autre types
    de pizza dans le menu.
    • En utilisant l’abstract factory, implémentez cette application.
"""

class Pizza:
    """
    Classe représentant une pizza
    """

    def __init__(self):
        self.etapes = []

    def preparer(self, patte, ingredients):
        print(f"préparation: patte {patte} et ingredient {', '.join(ingredients)}")

    def cuire(self, action):
        print(f"cuisson: {action}")

    def couper(self, action):
        """
        Méthode qui permet de couper la pizza
        :param action:
        :return:
        """
        print(f"coupe: {action}")

    def emballer(self, action):
        """
        Méthode qui permet d’emballer la pizza
        :param action:
        :return:
        """
        print(f"emballage: {action}")

# Menu de base de la pizzeria (à compléter)
menu = {
    "margarita": {
        "patte": "fine",
        "ingredients": ["tomate", "mozzarella"],
        "cuisson": "cuisson normale",
        "coupe": "coupe normale",
        "emballage": "emballage normale"
    },
    "4 fromages": {
        "patte": "fine",
        "ingredients": ["tomate", "mozzarella", "cheddar", "brie"],
        "cuisson": "cuisson normale",
        "coupe": "coupe normale",
        "emballage": "emballage normale"
    },
    "calzone": {
        "patte": "retourne",
        "ingredients": ["tomate", "mozzarella", "jambon", "champignon"],
        "cuisson": "cuisson normale",
        "coupe": "sans coupe",
        "embalage": "emballage pour calzone"
    },
    "hawaii": {
        "patte": "fine",
        "ingredients": ["tomate", "mozzarella", "ananas", "pomme de terre"],
        "cuisson": "cuisson normale",
        "coupe": "coupe normale",
        "emballage": "emballage normale"
    },
    "napolitaine": {
        "patte": "fine",
        "ingredients": ["tomate", "mozzarella", "jambon", "champignon"],
        "cuisson": "cuisson normale",
        "coupe": "coupe normale",
        "emballage": "emballage normale"
    }
}

class PizzaFactory:
    """
    Classe qui permet de fabriquer des pizzas
    """

    def __init__(self, menu):
        self.menu = menu

    def fabriquer(self, nom):
        """
        Méthode qui permet de fabriquer une pizza
        :param nom:
        :return:
        """
        pizza = Pizza()
        for etape in self.menu[nom]:
            if etape == "patte":
                pizza.preparer(self.menu[nom][etape], self.menu[nom]["ingredients"])
            elif etape == "cuisson":
                pizza.cuire(self.menu[nom][etape])
            elif etape == "coupe":
                pizza.couper(self.menu[nom][etape])
            elif etape == "emballage":
                pizza.emballer(self.menu[nom][etape])
        return pizza

if __name__ == "__main__":
    factory = PizzaFactory(menu)
    pizza = factory.fabriquer("margarita")
    print(pizza)
    pizza = factory.fabriquer("4 fromages")
    print(pizza)
    pizza = factory.fabriquer("calzone")
    print(pizza)
    pizza = factory.fabriquer("hawaii")
    print(pizza)
    pizza = factory.fabriquer("napoletana")
    print(pizza)
    pizza = factory.fabriquer("margarita")
    print(pizza)
    pizza = factory.fabriquer("4 fromages")
    print(pizza)
    pizza = factory.fabriquer("calzone")
    print(pizza)
    pizza = factory.fabriquer("hawaii")





def nouvelle_pizza(nom_recette, ingredients_suplementaires = []):
    """
    Crée une nouvelle pizza
    """
    if (nom_recette not in menu):
        raise ValueError(f"La recette {nom_recette} n'existe pas")
    recette = menu[nom_recette]
    pizza = Pizza()
    pizza.preparer(recette["patte"], recette["ingredients"]+ingredients_suplementaires)
    pizza.cuire(recette["cuisson"])
    pizza.couper(recette["coupe"])
    pizza.emballer(recette["emballage"])
    return pizza


if __name__ == "__main__":
    nouvelle_pizza("margarita", ["oeuf"])