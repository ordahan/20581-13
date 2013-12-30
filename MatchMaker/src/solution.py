'''
Created on Dec 22, 2013

@author: ord
'''
from random import shuffle


class Solution(object):
    '''
    Represents a single solution for the given matching problem.
    Contains a permutation of each of the categories we need
    to match together.
    '''

    def __init__(self, categories, categories_size, preferences):
        '''
        Creates a randome permutation for each of the categories given

        @categories - list of category names
        @categories_size - number of elements in each category
        '''
        self.category_size = categories_size
        self.categories = {}
        for category in categories:
            # Creates a list of all the elements in the category
            elements = range(categories_size)

            # Shuffle the elements randomly
            shuffle(elements)

            # Keep the random permutation created
            self.categories[category] = elements

        self.preferences = preferences
        self.fitness = self._evaluate()

        exit()

    def __str__(self):
        string_lines = []

        for i in xrange(self.category_size):
            match_element = []
            for elements in self.categories.values():
                match_element.append(str(elements[i]))
            string_lines.append('(' + ','.join(match_element) + ')')

        return ' '.join(string_lines)

    def crossover(self, other_solution):
        self._evaluate()
        return self

    def mutate(self):
        self._evaluate()
        pass


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
        print max_distance_from_preferences
        return max_distance_from_preferences

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
                    print self
                    # Get the distance of the given entity's matches from
                    # his preferences
                    id_of_current_entity_in_current_category = category_values[entity_id]
                    id_of_matched_entity_in_other_category = self.categories[other_category][entity_id]
                    preferences_for_current_entity = self.preferences[current_category][id_of_current_entity_in_current_category]
                    matched_entitiy_index_in_preferences = \
                        preferences_for_current_entity[other_category].index(id_of_matched_entity_in_other_category)
                    print matched_entitiy_index_in_preferences
                    distance += matched_entitiy_index_in_preferences
            exit()


    def _evaluate(self):
        return self._theoretical_non_tight_upper_bound_for_distance() - self._distance_from_optimal_solution()
