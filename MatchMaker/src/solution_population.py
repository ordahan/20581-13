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
        assert solutions is not None
        assert 0 <= mutation_rate <= 1
        assert 0 <= crossover_rate <= 1

        self.solutions = solutions
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def _create_selection_pool(self, solutions):

        assert len(solutions) > 0

        mating_pool_size = len(solutions) * 10
        probability_to_add = 0.5

        mating_pool = []

        while (len(mating_pool) < mating_pool_size):
            first, second = self._selection(solutions)

            if (random.random() < probability_to_add):
                if (first.fitness > second.fitness):
                    better_solution = first
                else:
                    better_solution = second

                mating_pool.append(better_solution)

        return mating_pool

    def _selection(self, pool):
        '''
        Select 2 solutions randomly
        '''
        first_solution = choice(pool)
        second_solution = choice(pool)
        return first_solution, second_solution


    def _crossover_with_probability(self, first_solution, second_solution):
        if (random.random() < self.crossover_rate):
            first_solution.crossover(second_solution)

        return first_solution


    def _mutate_with_probability(self, solution):
        if (random.random() < self.mutation_rate):
            solution.mutate()

        return solution

    def _generate_offsprings(self,
                             pool):
        next_generation = []

        for _ in xrange(len(self.solutions)):
            first_solution, second_solution = self._selection(pool)
            first_solution = first_solution.clone()
            second_solution = second_solution.clone()

            offspring = self._crossover_with_probability(first_solution,
                                                         second_solution)

            offspring_mutated = self._mutate_with_probability(offspring)

            next_generation.append(offspring_mutated)

        return next_generation

    def advance_generation(self):
        '''
        Advance a generation in the population
        '''
        selection_pool = self._create_selection_pool(self.solutions)

        self.solutions = self._generate_offsprings(selection_pool)

    def get_best_solution(self):
        # Sort the solutions by their fitness, place highest first
        self.solutions.sort(cmp=lambda x, y: x.fitness - y.fitness,
                            key=None,
                            reverse=True)
        return self.solutions[0]

    def __str__(self):
        return ' || '.join([str(solution.fitness) for solution in self.solutions])
