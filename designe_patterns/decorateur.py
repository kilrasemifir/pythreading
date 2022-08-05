"""
Exemple d'utilisation d'un design pattern Decorateur.
"""

class Coffee:
    """
    Un café
    """
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def describe(self):
        return "Coffee"


class BubbleTea:
    """
    Un café
    """
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def describe(self):
        return "Coffee"


class MilkToping:
    """
    Un toping de lait
    """
    def __init__(self, coffee):
        self.coffee = coffee

    def get_price(self):
        return self.coffee.get_price() + 0.5

    def describe(self):
        return f"{self.coffee.describe()} with milk"


class ChocolateToping:
    """
    Un toping de chocolat
    """
    def __init__(self, coffee):
        self.coffee = coffee

    def get_price(self):
        return self.coffee.get_price() + 1.0

    def describe(self):
        return f"{self.coffee.describe()} with chocolate"


class ChantillyToping:
    """
    Un toping de chantilly
    """
    def __init__(self, coffee):
        self.coffee = coffee

    def get_price(self):
        return self.coffee.get_price() + 1.5

    def describe(self):
        return f"{self.coffee.describe()} with chantilly"


mon_cafe = Coffee(1.0)
if input("Voulez vous du lait ? (y/n)") == "y":
    mon_cafe = MilkToping(mon_cafe)
if input("Voulez vous du chocolat ? (y/n)") == "y":
    mon_cafe = ChocolateToping(mon_cafe)
if input("Voulez vous du chantilly ? (y/n)") == "y":
    mon_cafe = ChantillyToping(mon_cafe)
print("Voici votre café : {}".format(mon_cafe.describe()))
print("Son prix est de {}".format(mon_cafe.get_price()))