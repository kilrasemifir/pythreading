from abc import ABC, abstractmethod


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def context_interface(self):
        self.strategy.algorithm_interface()

    def sort(self, list):
        self.strategy.sort(list)


class Strategy(ABC):
    @abstractmethod
    def sort(self, list):
        pass


class BubbleSort(Strategy):
    def sort(self, list):
        print("BubbleSort")
        print(list)
        for i in range(len(list)):
            for j in range(len(list) - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        print(list)


class QuickSort(Strategy):
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


context = Context(QuickSort())
context.sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])