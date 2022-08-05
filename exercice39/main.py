import time
from threading import Thread, Semaphore
from time import sleep

s_lire = Semaphore(1)
s_ecrire = Semaphore(1)

def reader(num,path):
    print(f"{num} :Je veux lire le fichier")
    with s_ecrire:
        print(f"{num} :En train de lire")
        with open(path, "r") as file:
            texte = file.read()
            print(f"{num} : {texte}")
        print(f"{num} :J'ai finis ma lecture")
        sleep(2)

def writer(num, path, texte):
    print(f"{num} :Je veux écrire dans le fichier")
    with s_lire and s_ecrire:
        print(f"{num} :En train d'écrire")
        with open(path, "a") as file:
            file.write(texte)
        print(f"{num} :J'ai finis d'écrire")
        sleep(2)

Thread(target=reader, args=(1,"test.txt",)).start()
Thread(target=reader, args=(2,"test.txt",)).start()
Thread(target=writer, args=(3,"test.txt", "hello",)).start()
Thread(target=writer, args=(4,"test.txt", "world!",)).start()
Thread(target=reader, args=(5,"test.txt",)).start()
