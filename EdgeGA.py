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
        self.cities = list(self.distances.keys())

        # Algorithm Parameters
        self.crossover_choice_p = 0.45
        self.crossover_rate = 0.7
        self.mutation_rate = 0.7
        self.mutation_weights = [2,5,3]
        self.pop_size = 2 * len(self.distances)
        self.num_children = self.pop_size // 3
        self.tournament_size = len(self.distances) // 10

        # Remember MST of map
        self.mst = galg.prims(self.distances)
        self.mst_cost = round(sum([self.distances[s][t] for s,t in self.mst]), 2)
        self.mst_dsum = round(galg.edge_apsp_sum(self.distances, self.mst), 2)

        # Generate the initial population, with a copy of mst in it
        population = [self.mst.copy()]
        while len(population) < self.pop_size:
            population.append(self.random_child())

        # The population is stored in a min heap to make mu-lambda
        # replacement faster
        id_function = lambda x : x['fitness']
        self.heap = MinHeap(id_function)
        for c in population: 
            self.heap.insert({'chr': c, 'fitness':self.fitness(c)})
  
    def main_loop(self):
        done = False
        while not done:
            for _ in range(self.num_children):
                c = self.new_child()
                fitness = self.fitness(c)
                if self.heap.heap[1]['fitness'] < fitness :
                    self.heap.extract()
                    self.heap.insert({'chr': c, 'fitness': fitness})
  
    def new_child(self) :
        p1 = self.tournament_select()
        child = p1
        if random.random() < self.crossover_rate:
            p2 = p1
            while p2 == p1:
                p2 = self.tournament_select()
            child = self.crossover(p1, p2)
        if random.random() < self.mutation_rate:
            child = self.mutate(child)
        return child

    def crossover(self, c1, c2):
        new_c = []
        for s,t in c1:
            if (s,t) in c2 or (t,s) in c2 or random.random() < self.crossover_choice_p:
                new_c.append((s,t))
        for s,t in c2:
            if (s,t) not in new_c and (t,s) not in new_c and random.random() < self.crossover_choice_p:
                new_c.append((s,t))
        return new_c

    def fitness(self, c):
        cost = sum([self.distances[s][t] for s,t in c])
        apsp_sum = galg.edge_apsp_sum(self.distances, c)
        if apsp_sum == float('inf'):
            return float("-inf")
#           apsp_sum = self.mst_dsum # result will be 0

#       included_vertices = []
#       for s,t in c:
#           if s not in included_vertices:
#               included_vertices.append(s)
#           if t not in included_vertices:
#               included_vertices.append(t)
#       base_score = round( len(self.cities) ** (len(included_vertices) / len(self.cities)), 2)
        base_score = 0

        return round( base_score + ((self.mst_dsum - apsp_sum) * self.mst_cost / cost), 2)

    def mutate(self, d):
        
    def mutate_add(self, d):
        c = d.copy()
        s,t = random.sample(self.cities, 2)
        while (s,t) not in c and (t,s) not in c:
            s,t = random.sample(self.cities, 2)
        c.append((s,t))
        return c

    def mutate_delete(self, d):
        c = d.copy()

        one_deg = []
        many_deg = []
        for pair in c:
            for city in pair:
                if city not in many_deg and city not in one_deg:
                    one_deg.append(city)
                elif city not in many_deg and city in one_deg:
                    one_deg.remove(city)
                    many_def.append(city)

        for idx in random.sample(range(len(c)), len(c)):
            if c[idx][0] in many_deg and c[idx][i] in many_deg:
                c.pop(idx)
                return c
                
    def mutate_split(self, d):
        c = d.copy()
        s,t = c.pop(random.choice(range(len(c))))
        u,v = random.sample(self.cities, 2)
        while (s,u) in c or (u,s) in c:
            u = random.sample(self.cities)
        while (t,v) in c or (v,t) in c:
            t = random.sample(self.cities)
        c.append((s,u))
        c.append((t,v))
        return c


    def random_child(self):
        return galg.randSpanningTree(list(self.distances.keys()))
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

    def tournament_selection(self):
        candidates = random.sample(self.heap.heap[1:], self.tournament_size)
        strongest = candidates[0]
        for candidate in candidates[1:]:
            if candidate['fitness'] > strongest['fitness']:
                strongest = candidate
        return strongest['chr']
