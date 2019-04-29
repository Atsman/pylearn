"""
Binary heap implementation.
"""


class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def from_list(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.head = [0] + alist[:]
        while (i > 0):
            self.percolate_down(i)
            i = i - 1

    def insert(self, k):
        self.heap_list.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def delete_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return retval

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
