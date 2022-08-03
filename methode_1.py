"""
Exemple de threading avec la methode fonctionnelle.
"""
from threading import Thread, get_ident
from time import sleep


def hello(message, delay):
    """Affiche un message avec un délai a l'infini"""
    while True:
        print(f"[{get_ident()}]:{message}")
        sleep(delay)


thread_1 = Thread(target=hello, args=("Hello", 1))
thread_1.start()
