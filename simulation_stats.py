import numpy as np
import matplotlib.pyplot as plt

def fitness_array(population):
        def get_fitness(i):
            return i.fitness


        # Sorry, used to JavaScript higher-order functions :/
        fitness_list = list(map(lambda i : get_fitness(i), population))
        return np.array(fitness_list)


def analyze_simulation(sim, iterations):
    # For simplicity, we only look at mean fitness over generation
    means = np.zeros([iterations])

    for i in range(iterations):
        means[i] = np.mean(fitness_array(sim.population))
        sim.iterate_generation()
        
    print(means)

    # plt.plot(means)
    # plt.xlabel('# generation')
    # plt.ylabel('mean fitness')
    # plt.show()