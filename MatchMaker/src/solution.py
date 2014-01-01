'''
Created on Dec 22, 2013

@author: ord
'''
from random import shuffle
import random


class Solution(object):
    '''
    Represents a single solution for the given matching problem.
    Contains a permutation of each of the categories we need
    to match together.
    '''

    def __init__(self, categories, categories_size, preferences, random=True):
        '''
        Creates a randome permutation for each of the categories given

        @categories - list of category names
        @categories_size - number of elements in each category
        '''
        self.category_size = categories_size
        self.categories = {}

        if (random):
            for category in categories:
                # Creates a list of all the elements in the category
                elements = range(categories_size)

                # Shuffle the elements randomly
                shuffle(elements)

                # Keep the random permutation created
                self.categories[category] = elements

        self.preferences = preferences

        # Using a roulette-wheel selection method means that we can
        # use the evaluation function as the fitness
        self.fitness = self._evaluate()

    def clone(self):
        clone = Solution(categories=self.categories.keys(),
                         categories_size=self.category_size,
                         preferences=self.preferences,
                         random=False)


        for category_name, values in self.categories.items():
            a = []
            a.extend(values)
            clone.categories[category_name] = a

        return clone

    def __str__(self):
        matches = []

        for i in xrange(self.category_size):
            match_element = []
            for elements in self.categories.values():
                match_element.append(str(elements[i]))
            matches.append('(' + ','.join(match_element) + ')')

        return '< Solution | Fitness: %d, Matches: %s>' % (self.fitness,
                                                           ' '.join(matches))

    def crossover(self, other_solution):

        # For each of the categories, select randomly
        # either this solution's values or the other one's
        for category_name in self.categories.keys():
            if (random.choice([True, False])):
                self.categories[category_name] = other_solution.categories[category_name]

        self.fitness = self._evaluate()

    def mutate(self):

        for _ in range(self.category_size / 10):
            category_to_mutate = random.choice(self.categories.values())
            first_match_index = random.randrange(self.category_size)
            second_match_index = random.randrange(self.category_size)

            # Swap the selection from the category for the matches chosen
            category_to_mutate[first_match_index], category_to_mutate[second_match_index] = \
                category_to_mutate[second_match_index], category_to_mutate[first_match_index]

        self.fitness = self._evaluate()

    def _theoretical_non_tight_upper_bound_for_distance(self):
        '''
        This is the worst situation that might happen,
        though it may not be actually possible (and probably will not)
        for each preferences given.
        '''
        # Match the entity with the worst matches on his preferences list
        worst_match_distance_for_entity = (self.category_size - 1) * (len(self.categories) - 1)
        # Match all the entities in the category with their worst matches
        worst_match_distance_for_category = self.category_size * worst_match_distance_for_entity
        # Match all the categories with their worst matches for all the entities
        max_distance_from_preferences = len(self.categories) * worst_match_distance_for_category

        return max_distance_from_preferences

    # TODO: WOW THATS UGLY SHIT
    def _distance_from_optimal_solution(self):
        distance = 0

        # Go over all the categories
        for current_category, category_values in self.categories.items():
            # Go over all the entities in the category
            # and calculate the distance from their optimal preference
            for entity_id in xrange(self.category_size):
                other_categories = [other_category
                                    for other_category in self.categories
                                    if other_category != current_category]
                # Go over the entity's matches from other categories
                for other_category in other_categories:
                    # Get the distance of the given entity's matches from
                    # his preferences
                    id_of_current_entity_in_current_category = category_values[entity_id]
                    id_of_matched_entity_in_other_category = self.categories[other_category][entity_id]

                    preferences_for_current_entity = self.preferences[current_category][id_of_current_entity_in_current_category]
                    matched_entity_index_in_preferences = \
                        preferences_for_current_entity[other_category].index(id_of_matched_entity_in_other_category)

                    distance += matched_entity_index_in_preferences

        return distance


    def _evaluate(self):
        max_worst_value = self._theoretical_non_tight_upper_bound_for_distance()
        distance_from_optimal_value = self._distance_from_optimal_solution()
        return max_worst_value - distance_from_optimal_value
