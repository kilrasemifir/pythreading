"""
Deuxieme methode pour la créaton de threads.
L'utilisation d'un sous-class de Thread.
"""
from threading import Thread
from time import sleep


class MonThread(Thread):
    """
    Exemple de threading avec une sous class de Thread.
    """
    def __init__(self, message, delay):
        super().__init__()
        self.message = message
        self.delay = delay

    def run(self):
        for i in range(10):
            print(f"{self.message}")
            sleep(self.delay)


class MonMultiThread(Thread):
    def __init__(self, messages, delays):
        super().__init__()
        self.messages = messages
        self.delays = delays

    def run(self):
        threads = []
        for message, delay in zip(self.messages, self.delays):
            th = MonThread(message, delay)
            th.start()
            threads.append(th)
        for th in threads:
            # Met en pause le thread courant (Ici MonMultiThread)
            # jusqu'a ce que le thread th soit terminé.
            th.join()
        print("STOP du Multithread")


if __name__ == "__main__":
    thread = MonMultiThread(["Hello", "Bonjour", "Salut"], [0.5, 0.7, 0.1])
    thread.start()