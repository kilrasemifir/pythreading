"""
Exemple de design pattern Composite.
"""


class Component:
    """
    Un composant de l'arbre.
    """
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def get_child(self, index):
        return self.children[index]

    def __repr__(self):
        return f"""{self.name}: [{", ".join(map(str, self.children))}]"""


voiture = Component("Voiture")
voiture.add(Component("Moteur"))
voiture.add(Component("Pneus"))
sieges = Component("Sieges")
sieges.add(Component("Siege 1"))
sieges.add(Component("Siege 2"))
voiture.add(sieges)

print(voiture)