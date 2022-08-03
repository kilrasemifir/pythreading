from threading import Thread
from time import sleep

def bouillir():
    print("Je fais bouillir de l'eau")
    sleep(3)


def ajouter_the(th1):
    th1.join()
    print("J'ajoute du the dans l'eau bouillante")
    sleep(3)


def ajouter_sucre(th1, sucre):
    if sucre:
        th1.join()
        print("J'ajoute du sucre dans l'eau bouillante")
        sleep(2)


def finir( th2, th3):
    th2.join()
    th3.join()
    print("J'ai fini de faire ma tasse")


sucre = False
task1 = Thread(target=bouillir)
# la virgule dans (task1,) permet de retourner un tuple et non task1 directement.
task2 = Thread(target=ajouter_the, args=(task1,))
task3 = Thread(target=ajouter_sucre, args=(task1, sucre))
task4 = Thread(target=finir, args=(task2, task3))


task1.start()
task2.start()
task3.start()
task4.start()

print("Je travaille")
print("J'attend mon the")