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

    def decrement(self, item, item_str, key_str):
        for entry, idx in enumerate(self.heap,1): 
            # must start at 1 because 0 is always none
            if entry[item_str] == item:
                entry[key_str] -= 1
                cur_idx = idx
                parent_idx = idx //2
                while parent_idx > 0 and self.heap[parent_idx][key_str] > self.heap[cur_idx][key_str]:
                    swap = self.heap[parent_idx]
                    self.heap[parent_idx] = self.heap[cur_idx]
                    self.heap[cur_idx] = swap
                return

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

class MaxHeap:
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
        largest  = i
        if l <= self.size and self.item_val(self.heap[l]) > self.item_val(self.heap[i]) :
            largest = l
        if r <= self.size and self.item_val(self.heap[r]) > self.item_val(self.heap[largest]) :
            largest = r
        if largest != i:
            item = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = item
            self.heapify(largest)

    def insert(self, item):
        self.size += 1
        self.heap.append(item) 
        i = self.size
        while i > 1 and self.item_val(self.heap[i]) > self.item_val(self.heap[i//2]):
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

