'''
Created on Dec 22, 2013

@author: ord
'''


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

    def run(self):
        pass
