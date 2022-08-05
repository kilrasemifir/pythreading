class ExecutorService:

    def __int__(self, nb_thread: int):
        self.nb_thread = nb_thread

    def submit(self, tache ) -> int:
        pass

    def remove(self, tache) -> bool:
        pass

    def is_finish(self, tache_id: int) -> bool:
        pass

    def shutdown(self) -> None:
        pass

