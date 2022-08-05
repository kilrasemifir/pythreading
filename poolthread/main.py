from concurrent.futures import ThreadPoolExecutor
from time import sleep


def hello(message):
    sleep(1)
    return f"Hello {message}"


with ThreadPoolExecutor(max_workers=1000) as executor:
    for i in range(1000):
        future = executor.submit(hello, i)
        # Block le currentThread tant que le thread n'est pas fini
        # print(future.result())

        # Execute la lambda quand le thread est fini.
        # Attention, cette fonction est appeler dans le future.
        future.add_done_callback(lambda f: print(f.result()))


thp = ThreadPoolExecutor(max_workers=100)
thp.submit(hello, "World")
thp.shutdown()

