import random
from collections import OrderedDict

class GA:
    def __init__(self):
        self.operators = []
        self.operator_weights = dict((op,1) for op in self.operators)
  
    def main_loop(self):
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

