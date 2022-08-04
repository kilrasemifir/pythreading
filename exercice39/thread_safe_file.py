from threading import Lock


class ThreadSafeFile:
    def __init__(self, filename: str):
        self.filename = filename
        self.read_lock = Lock()
        self.write_lock = Lock()

    def read(self):
        if not self.write_lock.locked():
            self.read_lock.acquire(blocking=False)
            with open(self.filename, "r") as f:
                return f.read()

    def write(self, text: str):
        with self.read_lock and self.write_lock:
            with open(self.filename, "w") as f:
                f.write(text)