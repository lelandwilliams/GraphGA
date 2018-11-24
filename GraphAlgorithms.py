from Heap import MinHeap
import random

# #######################################################
#       apsp - All Points Shortest Paths
#
#  given a graph represented as a matrix with
#  weighted edges, returns a matrix of 
#  shortes path lengths between  any pair of vertices
# #######################################################
def apsp(W):
    #
    # Inner Function Definitions
    #
    def newMatrix(size):
        M = []
        for _ in range(size):
            m = [float('inf')] * size
            M.append(m)
        return M

    def ExtendShortestPaths(L, a, b):
        if L[a] is None:
            L[a] = ExtendShortestPaths(L, a//2, a - a//2)
        if L[b] is None:
            L[b] = ExtendShortestPaths(L, b//2, b - b//2)
        n = len(l[a])
        M = newMatrix(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    M[i][j] = min(M[i][j], L[a][i][k] + L[b][k][j])
        return M
    
    #
    # Main function definition
    #

    n = len(W) -1 # since longest possible path is number of vertices -1
    L = [None] * (n+1) # initialzie L, the matrix of Matrix powers
    L[1] = W
    
    # Create L[0]
    
    l = newMatrix(n)
    for i in range(n):
        l[i][i] = 1
    L[0] = l
    
    L[n] = ExtendShortestPaths(L, n//2, n - n//2)
    return L
    
# ############################################################
#           prims.py
#  the prims() function takes as paremeters:
#
# D: a dictionary of key value pairs
# where the keys are labels of vertices, 
# and the values are dictionaries of labels - distance pairs
#
# returns an edge list unless to_graph is set to True
# ############################################################
def prims(D, start = None, to_graph = False, dist_graph = False): 
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
            for l in D.keys():
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

