"""
• Considérez une situation où nous avons un fichier partagé entre
plusieurs threads.
• Si l'une d’un thread essaie de modifier le fichier, aucune autre thread
ne doit être en train de lire ou d'écrire en même temps, sinon les
modifications ne lui seront pas visibles.
• Cependant, si un thread lit le fichier, d'autres peuvent le lire en même
temps.
• Implémentez cette application.
"""
def read(path):
    """
    Lit le fichier path et retourne le contenu.
    Si aucun autre thread n'est en train d'écrire, le contenu du fichier est lisible.
    Sinon il attend que les autres threads aient terminé d'écrire.
    :param path: chemin du fichier
    :return: contenu du fichier
    """
    pass


def write(path, text):
    """
    Ecrit le contenu text dans le fichier path.
    Si aucun autre thread n'est en train de lire ou ecrire, le contenu du fichier est modifiable.
    Sinon il attend que les autres threads aient terminé de lire ou d'écrire.
    :param path: chemin du fichier
    :param text: contenu du fichier
    :return: rien
    """
    pass
