'''
Created on Dec 27, 2013

@author: ord
'''
from random import choice
import random
import math


class SolutionPopulation(object):
    '''
    A population of solutions to a problem
    '''

    def __init__(self, solutions, crossover_rate, mutation_rate):
        assert solutions is not None
        assert 0 <= mutation_rate <= 1
        assert 0 <= crossover_rate <= 1

        self.solutions = solutions
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def _create_selection_pool(self, solutions):
        '''
        Create a 'roulette wheel pool' of solutions -
        the numer of times a solution will appear
        in the pool is determined by its relative fitness
        in the population.
        '''

        assert len(solutions) > 0

        total_population_fitness = sum([solution.fitness for solution in
                                        solutions])

        selection_pool = []
        for solution in solutions:
            selection_probability = (float(solution.fitness) / total_population_fitness)
            expected_number_of_offsprings = int(math.ceil(selection_probability * len(solutions)))
            for _ in range(expected_number_of_offsprings):
                selection_pool.append(solution)  # TODO: Is it ok to append multiple references?

        return selection_pool

    def _selection(self, pool):
        '''
        Select 2 solutions randomly
        '''
        first_solution = choice(pool)
        second_solution = choice(pool)
        return first_solution, second_solution


    def _crossover(self, first_solution, second_solution):
        if (random.random() < self.crossover_rate):
            new_solution = first_solution.crossover(second_solution)
        else:
            new_solution = first_solution
        return new_solution


    def _mutate(self, solution):
        if (random.random() < self.mutation_rate):
            solution.mutate()

    def _generate_offsprings(self,
                             pool):
        next_generation = []

        for _ in xrange(len(self.solutions)):
            first_solution, second_solution = self._selection(pool)

            new_solution = self._crossover(first_solution, second_solution)

            self._mutate(new_solution)

            next_generation.append(new_solution)

        return next_generation

    def advance_generation(self):
        '''
        Advance a generation in the population
        '''
        selection_pool = self._create_selection_pool(self.solutions)

        self.solutions = self._generate_offsprings(selection_pool)

        # Sort the solutions by their fitness
        self.solutions.sort(cmp=lambda x, y: x.fitness - y.fitness,
                            key=None,
                            reverse=False)

    def get_best_solution(self):
        return self.solutions[0]

    def __str__(self):
        return ' || '.join([str(solution) for solution in self.solutions])
