from threading import Thread, Lock
from time import sleep

voiture = Lock()
enfant = Lock()
def aller_parc():
    print("Je veux aller au parc")
    sleep(1)
    voiture.acquire()
    sleep(1)
    enfant.acquire(blocking=False)
    print("Je suis rentrée dans le parc")
    sleep(1)
    print("Je suis sortie du parc")
    enfant.release()
    voiture.release()

def aller_a_la_mairie():
    print("Je veux aller à la mairie")
    sleep(1)
    enfant.acquire()
    sleep(1)
    voiture.acquire(blocking=False)
    print("Je suis rentrée dans la mairie")
    sleep(1)
    print("Je suis sortie de la mairie")

    voiture.release()
    if enfant.locked():
        enfant.release()


Thread(target=aller_parc).start()
Thread(target=aller_a_la_mairie).start()