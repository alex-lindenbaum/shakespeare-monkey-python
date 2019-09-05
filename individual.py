import string
import random

from random_util import randomElement

class Individual:
    def __init__(self, target_dna, dna=''):
        if not dna:
            # For loading initial population
            # List over string because of mutability and traversal properties
            self.dna = '';
            for i in range(len(target_dna)):
                self.dna += (randomElement(string.printable))
        else:
            self.dna = dna

        self.fitness = self.evaluate_fitness(target_dna)


    def __str__(self):
        return self.dna
    

    def evaluate_fitness(self, target_dna):
        """
        Fitness: arbitrary measurment of survival and reproductive success for an individual.
        In this program, fitness is the proportion of dna chars that match in-place to target_dna.
        Takes on values dna: [0, 1].
        """
        matching_chars_freq = 0;
        dna_length = len(target_dna)
        for i in range(dna_length):
            if self.dna[i] == target_dna[i]:
                matching_chars_freq += 1

        return matching_chars_freq / dna_length


    def reproduce(self, other, mutation_rate, target_dna):
        """
        Two steps of sexual reproduction on the genetic level:
            1. Crossover: new individual gets a patch of both parents' dna
            2. Mutation: apply replacement mutation according to rate
        """

        # Crossover
        crossover_index = random.randint(0, len(self.dna))
        child_dna = self.dna[:crossover_index] + other.dna[crossover_index:]

        # Mutation
        if random.random() < mutation_rate:
            # This chance of this happening is mutation_rate
            child_dna_index = random.randint(0, len(child_dna) - 1)
            printable_index = random.randint(0, len(string.printable) - 1)

            child_dna = child_dna[:child_dna_index] + randomElement(string.printable) + child_dna[child_dna_index + 1:]

        return Individual(target_dna, child_dna)