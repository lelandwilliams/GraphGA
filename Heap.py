# ##############################
#           Heap.py
#
#  This file provide a MinHeap class.
#
#  The class constructor takes two optional
#  parameters: 
#    item_val, which is a lambda which
#       returns the value by which to sort the values
#    initial_list, a list of items to build a heap out of.
# ##############################

class HeapUnderflowError(Exception):
    pass

class MinHeap:
    def __init__(self, item_val = None, initial_list = None):
        self.heap = [None]
        self.size =  0
        if item_val is None:
            self.item_val = lambda x: x
        else:
            self.item_val = item_val
        if initial_list is not None:
            for item in initial_list:
                self.heap.append(item)
                self.size += 1
            for i in range(self.size//2,0,-1):
                self.heapify(i)

    def heapify(self, i = 1):
        l = 2 * i
        r = l + 1
        smallest  = i
        if l <= self.size and self.item_val(self.heap[l]) < self.item_val(self.heap[i]) :
            smallest = l
        if r <= self.size and self.item_val(self.heap[r]) < self.item_val(self.heap[smallest]) :
            smallest = r
        if smallest != i:
            item = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = item
            self.heapify(smallest)

    def insert(self, item):
        self.size += 1
        self.heap.append(item) 
        i = self.size
        while i > 1 and self.item_val(self.heap[i]) < self.item_val(self.heap[i//2]):
            swap_val = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = swap_val
            i = i//2

    def extract(self):
        if self.size < 1:
            raise HeapUnderflowError

        if self.size == 1:
            self.size = 0
            return self.heap.pop(-1)

        self.size -= 1
        swap_val = self.heap[1]
        self.heap[1] = self.heap.pop(-1)
        self.heapify()
        return swap_val

