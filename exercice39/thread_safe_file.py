"""
Correction de l'exercice page 39.
Voici l'énoncé de l'exercice:
• Considérez une situation où nous avons un fichier partagé entre
plusieurs threads.
• Si l'une d’un thread essaie de modifier le fichier, aucune autre thread
ne doit être en train de lire ou d’écrire en même temps, sinon les
modifications ne lui seront pas visibles.
• Cependant, si un thread lit le fichier, d’autres peuvent le lire en même
temps.
• Implémentez cette application.
"""
from threading import Lock
from json import load

class ThreadSafeFile:
    """
    Classe permettant d'avoir un acces concurrent sur un fichier.
    """
    def __init__(self, filename: str):
        """
        Constructeur de la classe.
        :param filename: chemain du fichier
        """
        self.filename = filename
        self.read_lock = Lock()
        self.write_lock = Lock()

    def read(self):
        """
        Lit le contenu du fichier.
        Si le fichier est en cours d'écriture, il attend que l'écriture se termine.
        :return: contenu du fichier
        """
        result = ""
        while True:
            if not self.write_lock.locked():
                self.read_lock.acquire(blocking=False)
                with open(self.filename, "r") as f:
                    result = f.read()
                if self.read_lock.locked():
                    self.read_lock.release()
                break
        return result

    def write(self, text: str):
        """
        Ecrit le contenu text dans le fichier.
        Si le fichier est en cours de lecture, il attend que la lecture se termine.
        Si un autre thread est en train d'écrire, il attend que l'écriture se termine.
        :param text: text a ajouter au fichier
        :return: rien
        """
        with self.read_lock and self.write_lock:
            with open(self.filename, "w") as f:
                print("Ajout dans le fichier", text)
                f.write(text)

    def append(self, text: str):
        """
        Ajoute le contenu text à la fin du fichier.
        Si le fichier est en cours de lecture, il attend que la lecture se termine.
        Si un autre thread est en train d'écrire, il attend que l'écriture se termine.
        :param text: text a ajouter au fichier
        :return: rien
        """
        with self.read_lock and self.write_lock:
            with open(self.filename, "a") as f:
                print("Ajout dans le fichier", text)
                f.write(text)
    def __enter__(self):
        """
        Permet de faire un with sur la classe.
        Pour ouvrir le fonctionnement de la classe, on ouvre les fichiers par exemple.
        :return:
        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Permet de faire un with sur la classe.
        Pour fermer le fonctionnement de la classe, on ferme les fichiers par exemple.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        pass


class ThreadSafeJson(ThreadSafeFile):
    """
    Classe permettant d'avoir un acces concurrent sur un fichier de type json.
    """
    def __init__(self, filename: str):
        super().__init__(filename)

    def read(self):
        """
        Lit le contenu du fichier et retourne un disctionnaire contenant les données du fichier json.
        :return: dictionnaire contenant les données du fichier json
        """
        result = super(ThreadSafeJson, self).read()
        return load(result)


if __name__ == "__main__":
    from threading import Thread
    nb_readers = 5
    nb_writers = 0
    nb_appenders = 5
    threads = []
    file = ThreadSafeFile("test.txt")
    for writer in range(nb_writers):
        threads.append(Thread(target=file.write, args=(f"Thread Writer {writer}",)))
    for appender in range(nb_appenders):
        threads.append(Thread(target=file.write, args=(f"Thread Appender {appender}",)))
    for reader in range(nb_readers):
        threads.append(Thread(target=lambda: print(f"Lecture du readers {reader} :\n{file.read()}")))
    for thread in threads:
        thread.daemon = True
        thread.start()
