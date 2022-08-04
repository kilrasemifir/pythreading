from threading import Thread, Semaphore
from time import sleep

voitures = Semaphore(1)


def prendre_la_voiture(nom):
    voitures.acquire()
    print(f"{nom} prend la voiture")
    sleep(2)
    print(f"{nom} laisse la voiture")
    voitures.release()

for i in range(5):
    Thread(target=prendre_la_voiture, args=(f"Thread {i}",)).start()