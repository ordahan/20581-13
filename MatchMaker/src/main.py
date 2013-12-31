'''
Created on Dec 22, 2013

@author: ord
'''
from matchmaker import MatchMaker

if __name__ == '__main__':
    print "Welcome to Match Maker, enjoy."
    MatchMaker(categories=['women', 'dogs', 'men'],
               category_size=50,  # 50,
               ).run(seconds_to_run=180,
                     crossover_rate=0.2,
                     mutation_rate=0.3,
                     generation_size=50,
                     best_result_fitness_print_interval=1)
