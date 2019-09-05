import numpy as np

from individual import Individual
from random_util import randomElement

class Simulation:
    def __init__(self, population_size, target_dna, survival_rate, mutation_rate):
        self.population_size = population_size
        self.target_dna = target_dna
        self.survival_rate = survival_rate
        self.mutation_rate = mutation_rate

        self.population = list();
        for i in range(population_size):
            self.population.append(Individual(target_dna))


    def iterate_generation(self):
        """
        Evolution process broken down into two parts:
            1. Natural selection: individual survive or die based on relative level of fitness
            2. Reproduction and death: survivors mate and die, next generation is born
        """

        # Natural selection
        self.apply_selection()

        # Reproduction and death
        if len(self.population) > 1:
            self.repopulate()
        else:
            # Every individual dies and no reproduction
            self.population = list()


    def sortByFitness(self):
        # Using this strategy hides implementation details
        def quicksort(arr=self.population):
            if len(arr) <= 1:
                return arr

            pivot = randomElement(arr)
            left = list()
            right = list()

            for individual in arr:
                if individual != pivot:
                    if individual.fitness <= pivot.fitness:
                        left.append(individual)
                    else:
                        right.append(individual)

            # Sort fitness largest to smallest
            return quicksort(right) + [pivot] + quicksort(left)


        self.population = quicksort()


    def apply_selection(self):
        # Left-most chunk of this list will be surviving population
        self.sortByFitness()

        separate_index = int(self.population_size * self.survival_rate)
        self.population = self.population[:separate_index]


    def repopulate(self):
        # All of previous generation die after reproducing
        next_generation = list()

        for i in range(self.population_size):
            # Algorithm is to select two random, distinct parents to reproduce
            parent_one = randomElement(self.population)
            parent_two = parent_one

            while parent_two == parent_one:
                parent_two = randomElement(self.population)

            child = parent_one.reproduce(parent_two, self.mutation_rate, self.target_dna)
            next_generation.append(child)

        self.population = next_generation