from threading import Thread
from time import sleep


def hello():
    while True:
        print("Hello")
        sleep(1)


th = Thread(target=hello)
th.daemon = True
th.start()
