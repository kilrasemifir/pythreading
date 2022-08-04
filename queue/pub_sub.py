import queue
from queue import Queue, LifoQueue
from threading import Thread


def producer(q):
    """
    Producer function
    """
    print("Je suis Ok")
    for i in range(10):
        print("Je suis en train de produire")
        q.put(input("Entrez un message: "))
        q.put("Hello world")


def consumer(queue, name):
    """
    Consumer function
    """
    while True:
        # queue.get() is a blocking call, so it will wait until there is something in the queue
        print(f"{name}:{queue.get()}")
        # queue.task_done() is a non-blocking call, so it will not wait until there is something in the queue
        # queue.task_done()
        # queue.join() is a blocking call, so it will wait until all the tasks in the queue are done
        # q.join()


q = Queue(maxsize=10)

Thread(target=producer, args=(q,)).start()
Thread(target=consumer, args=(q, "c1")).start()
Thread(target=consumer, args=(q, "c2")).start()

print(q.maxsize)

