from Heap import MinHeap
from collections import OrderedDict
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
def prims(D, start = None, to_matrix = False, dist_graph = False): 
    if start is None:
        start = random.choice(list(D.keys()))

    visited = [start]
    edges = []
    id_function = lambda x : x['weight']
    heap = MinHeap(item_val = id_function)
    for dest,dist in D[start].items():
        heap.insert({'origen':start, 'destination':dest, 'weight': dist})

    while heap.size > 0:
        e = None
        while e is None and heap.size > 0:
            e = heap.extract()
            if e['destination'] in visited:
                e = None

        if e is not None:
            v = e['destination']
            visited.append(v)
            edges.append(e)
            for dest,dist in list(D[v].items()):
                if dest in visited:
                    continue
                heap.insert({'origen':v, 'destination':dest, 'weight': dist})
            
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
                    M[e['destination']][e['origen']] = e['weight']
                else:
                    M[e['origen']][e['destination']] = 1
                    M[e['destination']][e['origen']] = 1

        return M

    return [(e['origen'],e['destination']) for e in edges] 

def randSpanningTree(initial_list):
    """ Returns a random spanning tree from a list of vertices.
        Based on prim's, but ignores weights """
    edges = []
    remaining = initial_list.copy()
    visited = [random.choice(remaining)]
    remaining.remove(visited[-1])

    while len(remaining) > 0:
        origen = random.choice(visited)
        destination = random.choice(remaining)
        remaining.remove(destination)
        edges.append((origen,destination))
        visited.append(destination)

    return edges

def edge2chr(clist, edgelist):
    """ takes a list of vertices, and a list of edges,
    and returns a list of the degrees of the vertices """
    d = OrderedDict()
    for c in clist:
        d[c] = 0
    for s,t in edgelist:
        d[s] += 1
        d[t] += 1

    return d
