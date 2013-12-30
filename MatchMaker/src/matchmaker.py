'''
Created on Dec 22, 2013

@author: ord
'''
from solution import Solution
import time
from solution_population import SolutionPopulation
from random import shuffle

class MatchMaker(object):
    '''
    Simulates match-making using genetic algorithms
    '''

    def __init__(self,
                 categories,
                 category_size):
        '''
        @categories - list of category names (example: ['men', 'women'])
        @category_size - number of elements in each of the categories,
        i.e: number of matches to be made.
        '''
        self.categories = categories
        self.category_size = category_size

    def run(self,
            seconds_to_run,
            best_result_fitness_print_interval=30,
            crossover_rate=0.5,
            mutation_rate=0.7,
            generation_size=100):
        '''
        @seconds_to_run - Number in seconds to run the algorithm
        @generation_size - how many solutions will there be in each
        generation of the genetic algorithm.
        @crossover_rate - probability of a crossover occuring
        @mutation_rate - probability of a mutation occuring

        '''
        # Generate a preference list for each of the categories
        preferences = {}
        for current_category in self.categories:
            # Generate preferences lists for each of the entities in the current current_category
            preferences_lists = {}
            for entity_id in xrange(self.category_size):
                # Generate a preference list - ranking the entities in all the other categories
                preference_list = {}
                other_categories = [other_category
                                    for other_category in self.categories
                                    if other_category != current_category]
                for other_category in other_categories:
                    # Generate a preference list that ranks a single current_category
                    preference_list[other_category] = range(self.category_size)
                    shuffle(preference_list[other_category])

                preferences_lists[entity_id] = preference_list
            preferences[current_category] = preferences_lists

        print "Preferences: ", preferences

        # Generate a pool of random possible population
        first_solution_generation = [Solution(categories=self.categories,
                                              categories_size=self.category_size,
                                              preferences=preferences)
                                     for _ in xrange(generation_size)]

        self.population = SolutionPopulation(solutions=first_solution_generation,
                                             crossover_rate=crossover_rate,
                                             mutation_rate=mutation_rate)


        # Run the genetic algorithm for the given number of seconds
        start_time = time.time()
        elapsed = 0
        time_to_print = 0
        while (elapsed < seconds_to_run):
            print self.population

            if (elapsed == time_to_print):
                time_to_print += best_result_fitness_print_interval

            # Iterate the algorithm
            self.population.advance_generation()

            # Count the running time
            elapsed = int(time.time() - start_time)
