import random
import GraphAlgorithms as galg
from collections import OrderedDict
from statistics import mean, stdev
from Heap import MaxHeap, MinHeap

class GA:
    def __init__(self, M):
        self.operators = []
        self.operator_weights = dict((op,1) for op in self.operators)
        self.generation = 0
        self.distances = M
        self.pop_size = 2 * len(self.distances)
        self.cities = list(self.distances.keys())
        self.num_children = self.pop_size // 3

        # Generate the initial population
        population = []
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
  
    def chr2edgelist(self, c):
        id_function = lambda x:x['deg']
        min_function = lambda x:x['dist']
        deg_heap = MaxHeap(id_function)
        degrees = {}
        E = []

        for city, deg in zip(self.cities, c):
            degrees[city] = deg
            deg_heap.insert({'v':city, 'deg':deg})

        while deg_heap.size > 0:
            s = deg_heap.extract()['v']
            dist_heap = MinHeap(min_function)
            for city, dist in self.distances[s].items():
                dist_heap.insert({'dest':city, 'dist':dist})
            while dist_heap.size > 0 and degrees[s] > 0:
                t = dist_heap.extract()['dest']
                if (s,t) not in E and (t,s) not in E and degrees[t] > 0:
                    E.append((s,t))
                    degrees[s] -= 1
                    degrees[t] -= 1

        return E

    def fitness(self, c):
        edgelist = self.chr2edgelist(c)
        M = galg.elist2matrix(self.distances, edgelist)
        return sum([sum(x) for x in M])

    def new_child(self):
        operator = random.choices(operator_weights.keys(), operator_weights.values())[0]
        child = operator()
        if child.fitness > self.min_fitness:
            operator_weights[operator] += 1
        return child

    def singlepoint_crossover(self):
        parent1 = self.tournament_selection()
        parent2 = self.tournament_selection(exclude=parent1)
        x_point = random.randint(0, parent1.size)
        return parent1[:x_point] + parent2[x_point:]

    def uniform_crossover(self):
        parent1 = self.tournament_selection()
        parent2 = self.tournament_selection(exclude=parent1)
        child = []
        i = 0
        for bit in random.choices([0,1] * self.size, self.size):
            if bit == 0:
                child.append(parent1[i])
            else:
                child.append(parent1[i])
            i += 1
        return child

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
        c = list(galg.edge2chr(self.cities, tree).values())
        most = num_cities - 1
        least = 0
        mode = most // 4
        num_increments = int(random.triangular(most, least, mode)) + 1
        idxs = random.choices(list(range(num_cities)), k = num_increments)
        for i in idxs:
            c[i] += 1

        return c



