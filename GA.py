import random
from collections import OrderedDict
from statistics import mean, stddev

class GA:
    def __init__(self, population):
        self.operators = []
        self.operator_weights = dict((op,1) for op in self.operators)
        self.generation = 0
        id_function = lambda x : x['fitness']
        self.heap = MinHeap(id_function)
        for c in population: 
            self.heap.insert({'chr': c, 'fitness':self.fitness(c)}
        self.num_children = self.heap.size() // 4
  
    def main_loop(self):
        done = False
        while not done:
            for in range(self.num_children):
                c = self.new_child()
                fitness = self.fitness(c)
                if self.heap.heap[1]['fitness'] < fitness :
                    self.heap.extract()
                    self.heap.insert({'chr': c, 'fitness': fitness})
        pass
  
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
        return patent1[:x_point] + parent2[x_point:]

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

