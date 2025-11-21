import math
import random


class MinHeap:
    def __init__(self):
        self.heapqueue = [1, 3, 3, 6, 9, 9, 5, 10, 7, 10]

    def __swap(self, i1, i2):
        temp = self.heapqueue[i1]
        self.heapqueue[i1] = self.heapqueue[i2]
        self.heapqueue[i2] = temp

    def insert(self, el):
        self.heapqueue.append(el)
        i = len(self.heapqueue) - 1
        parent_i = math.floor((i - 1) / 2)
        while (
            i >= 0
            and parent_i >= 0
            and self.heapqueue[i] < self.heapqueue[parent_i]
        ):
            # print(
            #     f"curr {i}: {self.heapqueue[i]}, parent: {parent_i}: {self.heapqueue[parent_i]}"
            # )
            self.__swap(i, parent_i)
            i = parent_i
            parent_i = math.floor((i - 1) / 2)
        return

    def seek(self):
        return self.heapqueue[0]

    def extract(self):
        self.__swap(0, len(self.heapqueue) - 1)
        min_el = self.heapqueue.pop()
        i = 0
        child1 = 2 * i + 1
        child2 = 2 * i + 2
        while (
            i < len(self.heapqueue)
            and child1 < len(self.heapqueue)
            and child2 < len(self.heapqueue)
            and (
                self.heapqueue[i] > self.heapqueue[child1]
                or self.heapqueue[i] > self.heapqueue[child2]
            )
        ):
            min_child = -1
            if self.heapqueue[child1] > self.heapqueue[child2]:
                min_child = child2
            else:
                min_child = child1
            self.__swap(i, min_child)
            i = min_child
            child1 = 2 * i + 1
            child2 = 2 * i + 2
        return min_el

    def print_heap(self):
        print(self.heapqueue)


if __name__ == "__main__":
    minheap = MinHeap()
    for i in range(8):
        minheap.extract()
        minheap.print_heap()
    # minheap.insert(2)
    # minheap.print_heap()
