"""
Title: Shakespeare Monkey
Author: Alexander Lindenbaum
"""

from simulation import Simulation
from simulation_stats import analyze_simulation

if __name__ == '__main__':

    # Use this space to create simulations and analyze how the population's avg. fitness changes over time.

    sim = Simulation(500, 'this is a test target_dna', 0.3, 0.01)
    analyze_simulation(sim, 100)

    sim = Simulation(500, 'longer target_dnas are more representative of evolution with regards to the human genome', 0.4, 0.05)
    analyze_simulation(sim, 200)