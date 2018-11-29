import random
import GraphAlgorithms as galg
from collections import OrderedDict
from statistics import mean, stdev
from Heap import MaxHeap, MinHeap

class EdgeGA:
    def __init__(self, distances_matrix):
        self.distances = distances_matrix
        self.name = "Edge GA"
        self.generation = 0
        self.pop_size = 2 * len(self.distances)
        self.cities = list(self.distances.keys())
        self.num_children = self.pop_size // 3

        # Remember MST version of 
        self.mst = galg.prims(self.distances)
        self.mst_cost = sum([self.distances[s][t] for s,t in self.mst])
        #A = galg.edge_apsp(self.distances, self.mst)
        #self.mst_dsum = round(sum([sum(x) for x in A]),2 )
        self.mst_dsum = round(galg.edge_apsp_sum(self.distances, self.mst), 2)

        # Generate the initial population, with a copy of mst in it
        population = [self.mst.copy()]
        while len(population) < self.pop_size:
            population.append(self.random_child())

        # The population is stored in a min heap to make mu-lambda
        # replacement faster
        id_function = lambda x : x['fitness']
        self.heap = MinHeap(id_function)
#        for c in population: 
#            self.heap.insert({'chr': c, 'fitness':self.fitness(c)})
  
    def main_loop(self):
        done = False
        while not done:
            for _ in range(self.num_children):
                c = self.new_child()
                fitness = self.fitness(c)
                if self.heap.heap[1]['fitness'] < fitness :
                    self.heap.extract()
                    self.heap.insert({'chr': c, 'fitness': fitness})
        pass
  
    def fitness(self, c):
        cost = sum([self.distances[s][t] for s,t in c])
        apsp_sum = galg.edge_apsp_sum(self.distances, c)
        if apsp_sum == float('inf'):
            apsp_sum = self.mst_dsum # result will be 0

        included_vertices = []
        for s,t in c:
            if s not in included_vertices:
                included_vertices.append(s)
            if t not in included_vertices:
                included_vertices.append(t)
        base_score = round( len(self.cities) ** (len(included_vertices) / len(self.cities)), 2)

        return round( base_score + ((self.mst_dsum - apsp_sum) * self.mst_cost / cost), 2)

    def mutate(self, child = None):
        if child is None:
            child = self.tournament_selection()
        gene1, gene2 = random.sample(list(range(len(child))), 2)
        max_size = len(child) -1

        if child[gene1] == max_size:
            child[gene1] -= 1
        elif child[gene1] == 1:
            child[gene1] = 2
        else:
            child[gene1] += random.choice([-1, +1])

        if child[gene2] == max_size:
            child[gene2] -= 1
        elif child[gene2] == 1:
            child[gene2] = 2
        else:
            child[gene2] += random.choice([-1, +1])

        return child

    def random_child(self):
        num_cities = len(self.distances)
        #c = [1] * num_cities
        tree = galg.randSpanningTree(list(self.distances.keys()))
        c = galg.edge2chr(self.cities, tree)
        most = num_cities - 1
        least = 0
        mode = most // 4
        num_increments = int(random.triangular(most, least, mode)) + 1
        idxs = random.choices(list(range(num_cities)), k = num_increments)
        for i in idxs:
            c[i] += 1

        return c



