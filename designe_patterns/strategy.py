"""
Exemple de design pattern Strategy.

Dans cette exemple on va voir comment on peut changer de strategie pour le tri de liste grace au pattern strategy.
"""
from abc import ABC, abstractmethod


class Context:
    """
    Le context joue le role de l'interface du pattern strategy.
    """
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, list):
        """
        Methode metier du context.
        Elle permet de lancer le tri de la liste en fonction de la strategie choisi.
        :param list: liste a trier
        :return: liste triee
        """
        self.strategy.sort(list)


class Strategy(ABC):
    """
    Une strategy contient l'algorithme de tri.
    """
    @abstractmethod
    def sort(self, list):
        """
        Methode de trie a implémenter pour la création de la strategie.
        :param list: liste a trier
        :return: liste triee
        """
        pass


class BubbleSort(Strategy):
    """
    Strategy de try en utilisant l'algorithme de tri bubble sort.
    """
    def sort(self, list):
        print("BubbleSort")
        print(list)
        for i in range(len(list)):
            for j in range(len(list) - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        print(list)


class QuickSort(Strategy):
    """
    Strategy de try en utilisant l'algorithme de tri quick sort.
    """
    def sort(self, list):
        print("QuickSort")
        print(list)
        self.quickSort(list, 0, len(list) - 1)
        print(list)

    def quickSort(self, list, start, end):
        if start < end:
            pivot = self.partition(list, start, end)
            self.quickSort(list, start, pivot - 1)
            self.quickSort(list, pivot + 1, end)

    def partition(self, list, start, end):
        pivot = list[end]
        i = start - 1
        for j in range(start, end):
            if list[j] <= pivot:
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i + 1], list[end] = list[end], list[i + 1]
        return i + 1


class MergeSort(Strategy):
    """
    Strategy de try en utilisant l'algorithme de tri merge sort.
    """
    def sort(self, list):
        print("MergeSort")
        print(list)
        self.mergeSort(list, 0, len(list) - 1)
        print(list)

    def mergeSort(self, list, start, end):
        if start < end:
            mid = (start + end) // 2
            self.mergeSort(list, start, mid)
            self.mergeSort(list, mid + 1, end)
            self.merge(list, start, mid, end)

    def merge(self, list, start, mid, end):
        left = list[start:mid + 1]
        right = list[mid + 1:end + 1]
        i = j = 0
        k = start
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    list = [3, 1, 2, 5, 4]
    context = Context(BubbleSort())
    context.sort(list)
    context.strategy = QuickSort()
    context.sort(list)
    context.strategy = MergeSort()
    context.sort(list)
    print(list)