from threading import Thread,Lock,Semaphore
from time import sleep
"""
Dans ce script
Thread i lire
Thread iX viens pour ecrire il dois attend Thread i fini mais il block l'autre access a lire... 
Thread nX viens il ne peut pas lire parce qu'il y a un lock
Thread i finir a lire et deblock access a lire
Thread iX ecrires et deblock la lock access write et read
Thread nX lire
"""
access_lock = Lock()
access_semaphore = Semaphore(2)

def read (nom,path):
    """Lit le fichieur path et retourne le contenu"""
    result = ""
    access_semaphore.acquire()
    # print(f"{nom} prend la fichier")
    with open(path, 'r') as file:
        content = file.read()
        result = content
        sleep(2)
    access_semaphore.release()
    return result

def write (nom,path, content):
    access_semaphore.acquire(blocking=True)
    access_lock.acquire()
    """Ecrit le contenu dans le fichier path"""
    with open(path, 'a') as file:
        file.write(content)
        sleep(2)
    print(f"{nom} prend la fichier")
    access_lock.release()
    access_semaphore.release()

if __name__ == "__main__":
    from threading import Thread
    nb_readers = 5
    nb_writers = 2
    threads = []
    path = "test.txt"
    for reader in range(nb_readers):
        threads.append(Thread(target=lambda: print(f"Lecture du readers {reader} :\n{read(reader, path)}")))

    for writer in range(nb_writers):
        threads.append(Thread(target=write, args=(writer, path, f"Thread Writer {writer}",)))
    for thread in threads:
        thread.start()
