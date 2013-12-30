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

    def _evaluate(self):
        return 1
