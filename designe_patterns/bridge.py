"""
Exemple de design pattern Bridge.

Le design pattern Bridge permet de créer des objets qui sont "liés" entre eux.
"""
class CuboidAPI1:
    def produce(self, length, width, height):
        print(f"Produce a cuboid of length {length}, width {width} and height {height} Avec l'API 1")


class CuboidAPI2:
    def produce(self, length, width, height):
        print(f"Produce a cuboid of length {length}, width {width} and height {height} Avec l'API 2")


class CuboidAPI3:
    def produce(self, length, width, height):
        print(f"Produce a cuboid of length {length}, width {width} and height {height} Avec l'API 3")


class CuboidBridge:
    def __init__(self, length, width, height, api):
        self.length = length
        self.width = width
        self.height = height
        self.api = api

    def produce(self):
        self.api.produce(self.length, self.width, self.height)


api1 = CuboidAPI1()
cuboid1 = CuboidBridge(10, 20, 30, api1)
cuboid1.produce()

api2 = CuboidAPI2()
cuboid2 = CuboidBridge(10, 20, 30, api2)
cuboid2.produce()