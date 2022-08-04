from os import listdir, path
from threading import Thread


class FileInfo(Thread):
    """Thread pour afficher le nombre de caractères d'un fichier et leurs répartition dans un fichier texte"""
    def __init__(self, path):
        Thread.__init__(self)
        self.path = path

    def run(self):
        """Methode appelé lors du lancement du thread"""
        with open(self.path, "r", encoding="utf-8") as f:
            texte = f.read()
            taille = len(texte)
            print(f"{self.path} : {taille} caractères et : {self.count_char(texte)}")

    def count_char(self, text):
        """
        Retourne le nombre de caractères d'un texte
        :param text: texte a analyser
        :return: dictionnaire contenant la liste des charactères et leur nombre d'apparition
        """
        result = {}
        for char in text.lower():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
        return result


def find_file_paths(root_path=".", file_extension=".txt"):
    """
    Retourne la liste des fichiers contenus dans le dossier root_path.
    :param root_path: dossier racine ou effectuer la recherche
    :param file_extension: extension des fichiers a rechercher
    :return: la liste des fichiers dans le dossier root_path finissant par l'extension file_extension
    """
    results = []
    for file_path in listdir(root_path):
        if path.isfile(file_path) and file_path.endswith(file_extension):
            results.append(file_path)
    return results


if __name__ == "__main__":
    for file_path in find_file_paths():
        thread = FileInfo(file_path)
        thread.start()
