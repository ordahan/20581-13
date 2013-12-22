'''
Created on Dec 22, 2013

@author: ord
'''
from matchmaker import MatchMaker

if __name__ == '__main__':
    MatchMaker(categories=['women', 'dogs', 'men'],
               items_per_category=5,  # 50,
               generation_size=5).run(180)  # 180 seconds = 3 mins
