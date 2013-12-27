'''
Created on Dec 27, 2013

@author: ord
'''
from random import choice
import random


class SolutionPopulation(object):
    '''
    A population of solutions to a problem
    '''

    def __init__(self, solutions, crossover_rate, mutation_rate):
        self.solutions = solutions
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    @staticmethod
    def _create_mating_pool(solutions):
        '''
        Create a 'roulette wheel pool' of solutions -
        the numer of times a solution will appear
        in the pool is determined by its relative fitness
        to the population.
        '''
        total_population_fitness = sum([solution.fitness for solution in
                                        solutions])

        return [solution * (solution.fitness / total_population_fitness)
                for solution in solutions]

    @staticmethod
    def _crossovers(pool,
                    desired_number_of_crossovers,
                    crossover_rate):
        next_generation = []

        for _ in xrange(desired_number_of_crossovers):
            # Select 2 solutions randomly
            first_solution = choice(pool)
            second_solution = choice(pool)
            # Crossover
            if (random.random() < crossover_rate):
                new_solution = first_solution.crossover(second_solution)
            else:
                new_solution = first_solution
            # Add to the next generation
            next_generation.append(new_solution)

        return next_generation


    @staticmethod
    def _mutations(solutions,
                   mutation_rate):

        assert 0 <= mutation_rate <= 1

        for solution in solutions:
            if (random.random() < mutation_rate):
                solution.mutate()

    def advance_generation(self):
        '''
        Advance a generation in the population
        '''
        mating_pool = self._create_mating_pool(self.solutions)

        solutions_next_generation = self._crossovers(mating_pool,
                                                    len(self.solutions))

        self.solutions = self._mutations(solutions_next_generation)
