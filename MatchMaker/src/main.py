'''
Created on Dec 22, 2013

@author: ord
'''
from matchmaker import MatchMaker

if __name__ == '__main__':
    print "Welcome to Match Maker, enjoy."

    import cProfile

    profiler = cProfile.Profile()


    # Print with random preferences each time
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~ Random preferences ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for _ in range(10):
        MatchMaker(categories=['women', 'dogs', 'men'],
               category_size=50,
               ).run(seconds_to_run=180,
                     crossover_rate=0.8,
                     mutation_rate=0.3,
                     generation_size=40,
                     best_result_distance_print_interval=30)
        print

    # Print with constant preferences each time
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~ Constant preferences ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    match_const_preferences = MatchMaker(categories=['women', 'dogs', 'men'],
                                         category_size=50)
    for _ in range(10):
        match_const_preferences.run(seconds_to_run=180,
                                     crossover_rate=0.8,
                                     mutation_rate=0.3,
                                     generation_size=40,
                                     best_result_distance_print_interval=30)
        print
