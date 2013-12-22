'''
Created on Dec 22, 2013

@author: ord
'''
from solution import Solution
import time


class MatchMaker(object):
    '''
    Simulates match-making using genetic algorithms
    '''

    def __init__(self, categories, items_per_category, generation_size=100):
        '''
        @categories - list of category names (example: ['men', 'women'])
        @items_per_category - number of elements in each of the categories,
        i.e: number of matches to be made.
        @generation_size - how many 'solutions' will there be for each
        generation of the genetic algorithm.
        '''
        self.categories = categories
        self.items_per_category = items_per_category
        self.generation_size = generation_size

    def run(self, seconds_to_run):
        '''
        @seconds_to_run - Number in seconds to run the algorithm
        '''
        # Generate a pool of random possible solutions
        self.solutions = \
            [Solution(categories=self.categories,
                      categories_size=self.items_per_category)
             for _ in xrange(self.generation_size)]

        # Run the genetic algorithm for the given number of seconds
        start_time = time.time()
        elapsed = 0
        while (elapsed < seconds_to_run):
            # Iterate the algorithm
            self.solutions = self.get_next_generation(self.solutions)

            # Count the running time
            elapsed = time.time() - start_time

    def get_next_generation(self, solutions):
        pass
