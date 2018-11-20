# ##############################
#           prims.py
#  the prims() function takes as paremeters:
#
# D: a dictionary of key value pairs
# where the keys are labels of vertices, 
# and the values are dictionaries of labels - distance pairs
#
# returns an edge list unless to_graph is set to True
# ##############################

from Heap import MinHeap
import random

def prims(self, D, start = None. to_graph = False, dist_graph = False): 
    if start is None:
        start = random.selection(D.keys())

    visited = [start]
    edges = []
    id_function = lambda x : x['weight']
    heap = MinHeap(item_val = id_function)

    for v in D.keys():
        if v in visited:
            continue
        for dest,dist in D[v].iteritems():
            if dest in visited:
                continue
            heap.insert({'origen':v, 'destination':dest, 'weight': dist})
        e = None
        while e is None:
            e = heap.extract()
            if e['destination'] in visited:
                e = None
        edges.append(e)

    if to_matrix:
        # initialize M
        M = {}
        for k in D.keys():
            M[k] = {}
            for l in D.keys()
                if dist_graph:
                    M[k][l] = float('inf')
                else:
                    M[k][l] = 0

        for e in edges:
                if dist_graph:
                    M[e['origen']][e['destination']] = e['weight']
                else:
                    M[e['origen']][e['destination']] = 1

        return M

    return edges


