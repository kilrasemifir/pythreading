"""

"""
from threading import Thread
from time import sleep
from methode_2 import MonThread


def print_message(message, delay):
    """
    Affiche un message avec un délai a l'infini
    :param message: message a afficher
    :param delay: délai entre chaque affichage du message
    :return: rien
    """
    while True:
        print(f"{message}")
        sleep(delay)


def message_multipthread(messages, delays):
    """
    Créer pour chaque message et chaque delay un thread qui affiche le message toute les delay secondes.
    :param messages: liste de messages a afficher
    :param delays: delays pour chaque messages. Doit etre de même taille que messages.
    :return: rien
    """
    if len(messages) != len(delays):
        raise ValueError(f"""Les parametres messages et delays doivent avoir la même taille.
        >> ici messages est de taille {len(messages)} et delays est de taille {len(delays)}""")
    for message, delay in zip(messages, delays):
        thread = MonThread(message, delay)
        thread.start()


messages = [
    "Hello",
    "Bonjour",
    "Salut",
]

delays = [
    0.5,
    0.7,
    1.5,
]

message_multipthread(messages, delays)