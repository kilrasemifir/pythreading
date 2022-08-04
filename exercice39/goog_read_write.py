from threading import Lock


class BetterThreadSafeFile:
    """
    Meilleur solution pour la lecture et l'écriture d'un fichier thread safe.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.nombre_de_lecteur = 0
        self.lock_preventif = Lock()
        self.lock_ecriture = Lock()

    def read(self):
        """
        Lit le contenu du fichier.
        Si le fichier est en cours d'écriture, il attend que l'écriture se termine.
        :return: le contenu du fichier
        """
        with self.lock_preventif:
            self.nombre_de_lecteur += 1
            if self.nombre_de_lecteur == 1:
                self.lock_ecriture.acquire()

        with open(self.filename, "r") as f:
            result = f.read()

        with self.lock_preventif:
            self.nombre_de_lecteur -= 1
            if self.nombre_de_lecteur == 0:
                self.lock_ecriture.release()

        return result

    def write(self, text: str):
        """
        Ecrit le contenu text dans le fichier.
        Si le fichier est en cours de lecture, il attend que la lecture se termine.
        :param text: text a ajouter au fichier
        :return: rien
        """
        with self.lock_ecriture:
            with open(self.filename, "w") as f:
                print("Ajout dans le fichier", text)
                f.write(text)