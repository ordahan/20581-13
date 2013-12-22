'''
Created on Dec 22, 2013

@author: ord
'''
from solution import Solution
import time
from random import random, choice


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
        self.items_per_category = category_size
        self.generation_size = generation_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def run(self, seconds_to_run):
        '''
        @seconds_to_run - Number in seconds to run the algorithm
        '''
        # Generate a pool of random possible population
        self.population = \
            [Solution(categories=self.categories,
                      categories_size=self.items_per_category)
             for _ in xrange(self.generation_size)]

        # Run the genetic algorithm for the given number of seconds
        start_time = time.time()
        elapsed = 0
        while (elapsed < seconds_to_run):
            # Iterate the algorithm
            self.population = self.get_next_generation(self.population)

            # Count the running time
            elapsed = time.time() - start_time

    def get_next_generation(self, population):

        # Get the total fitness of the population
        total_fitness = sum([solution.fitness
                             for solution
                             in population])

        # Create a 'roulette wheel pool' of solutions
        # to choose solutions that will contribute to the
        # next generation
        mating_pool = [solution * (solution.fitness / total_fitness)
                       for solution
                       in population]

        next_generation = []

        for _ in xrange(len(population)):
            # Select randomly 2 solutions
            first_solution = choice(mating_pool)
            second_solution = choice(mating_pool)

            # Crossover
            if (random.random() < self.Pcrossover):
                new_solution = first_solution.crossover(second_solution)
            else:
                new_solution = first_solution

            # Mutate
            if (random.random() < self.Pmutate):
                new_solution.mutate()

            # Add to the next generation
            next_generation.append(new_solution)
