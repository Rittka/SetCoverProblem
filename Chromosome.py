import Population
import random

class Chromosome:
    list_Gene = list()
    cost_Ch = 0
    count_subSets = 0
    fitness_value = 0.0
    population = Population.Population()
         
    
    def __init__(self):
        for j in range(population.numOfSubsets):
            self.list_Gene.append(random.choice([0,1]))






  
      