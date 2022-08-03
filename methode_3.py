"""
Threading avec class mais sans etre une sous class de Thread.
"""
from threading import Thread
from time import sleep


class MessagePrinter:
    """Classe permettant d'afficher en boucle un message avec un délai a l'infini"""
    def __init__(self, message, delay):
        self.message = message
        self.delay = delay

    def print(self):
        """Affiche un message avec un délai a l'infini"""
        for i in range(10):
            print(f"{self.message}")
            sleep(self.delay)


message_printer = MessagePrinter("Hello", 1)
thread = Thread(target=message_printer.print)
thread.start()
