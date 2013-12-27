'''
Created on Dec 22, 2013

@author: ord
'''
from solution import Solution
import time
from solution_population import SolutionPopulation

class MatchMaker(object):
    '''
    Simulates match-making using genetic algorithms
    '''

    def __init__(self,
                 categories,
                 category_size,
                 crossover_rate,
                 mutation_rate,
                 generation_size=100):
        '''
        @categories - list of category names (example: ['men', 'women'])
        @category_size - number of elements in each of the categories,
        i.e: number of matches to be made.
        @generation_size - how many solutions will there be in each
        generation of the genetic algorithm.
        @crossover_rate - probability of a crossover occuring
        @mutation_rate - probability of a mutation occuring
        '''
        self.categories = categories
        self.category_size = category_size
        self.generation_size = generation_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def run(self, seconds_to_run):
        '''
        @seconds_to_run - Number in seconds to run the algorithm
        '''
        # Generate a pool of random possible population
        self.population = SolutionPopulation(solutions=[Solution(categories=self.categories,
                                                                 categories_size=self.category_size)
                                                        for _ in xrange(self.generation_size)],
                                             crossover_rate=self.crossover_rate,
                                             mutation_rate=self.mutation_rate)


        # Run the genetic algorithm for the given number of seconds
        start_time = time.time()
        elapsed = 0
        while (elapsed < seconds_to_run):
            # Iterate the algorithm
            self.population.advance_generation()

            # Count the running time
            elapsed = time.time() - start_time
