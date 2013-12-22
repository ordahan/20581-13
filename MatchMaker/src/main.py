'''
Created on Dec 22, 2013

@author: ord
'''
from matchmaker import MatchMaker

if __name__ == '__main__':
    MatchMaker(categories=['women', 'dogs', 'men'],
               items_per_category=50,
               generation_size=100).run()
