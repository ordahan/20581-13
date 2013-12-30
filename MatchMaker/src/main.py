'''
Created on Dec 22, 2013

@author: ord
'''
from matchmaker import MatchMaker

if __name__ == '__main__':
    print "Welcome to Match Maker, enjoy."
    MatchMaker(categories=['women', 'dogs', 'men'],
               category_size=3,  # 50,
               ).run(seconds_to_run=5,
                     crossover_rate=1,
                     mutation_rate=1,
                     generation_size=3,
                     best_result_fitness_print_interval=1)  # 180 seconds = 3 mins
