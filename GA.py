import random
from collections import OrderedDict
from statistics import mean, stdev

class GA:
    def __init__(self, population):
        self.operators = []
        self.operator_weights = dict((op,1) for op in self.operators)
        self.generation = 0
        id_function = lambda x : x['fitness']
        self.heap = MinHeap(id_function)
        for c in population: 
            self.heap.insert({'chr': c, 'fitness':self.fitness(c)})
        self.num_children = self.heap.size() // 4
  
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

    def add_mutation(self, child = None, genes = None):
        if child is None:
            child = self.tournament_selection()
        if genes is None:
            gene1, gene2 = random.sample(list(range(len(child))), 2)
        else:
            gene1, gene2 = genes
        max_size = len(child) -1
        if child[gene1] == max_size or child[gene2] == max_size:
            return self.move_mutation(child, (gene1,gene2))
        child[gene1] += 1
        child[gene2] += 1
        return child

    def del_mutation(self, child = None, genes = None):
        if child is None:
            child = self.tournament_selection()
        if genes is None:
            gene1, gene2 = random.sample(list(range(len(child))), 2)
        else:
            gene1, gene2 = genes
        min_size = 1
        if child[gene1] == min_size or child[gene2] == min_size:
            return self.move_mutation(child)
        child[gene1] -= 1
        child[gene2] -= 1
        return child

    def move_mutation(self, child = None, genes = None):
        if child is None:
            child = self.tournament_selection()
        if genes is None:
            gene1, gene2 = random.sample(list(range(len(child))), 2)
        else:
            gene1, gene2 = genes
        gene1, gene2 = random.sample(list(range(len(child))), 2)
        min_size = 1
        if child[gene1] == min_size and child[gene2] == min_size:
            return self.add_mutation(child)
        if child[gene1] == min_size and child[gene2] == min_size:
            return self.add_mutation(child)
        child[gene1] -= 1
        child[gene2] -= 1
        return child


