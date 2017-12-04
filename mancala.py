'''
Python implementation of Mancala
'''

import re
import os
import time
import sys
import subprocess


# constants


def timing_function(timed_function):
    ''' Outputs time a function takes to execute '''
    def wrapper():
        ''' wrapper '''
        t_start = time.time()
        timed_function()
        t_end = time.time()
        return 'Script ran for {} seconds\n'.format(str((t_end - t_start)))
    return wrapper


@timing_function
def main():
    ''' main function '''
    m = Mancala('M')
    m.dump_status()



# http://www.pressmantoy.com/game-rules/Mancala_rules.pdf
# http://www.ultraboardgames.com/mancala/game-rules.php

class Mancala(object):
    ''' mancala container '''
    def __init__(self, name):
        ''' constructor '''
        self._pits = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self._player_A_store = 0
        self._player_B_store = 0
    def dump_status(self):
        ''' outputs text status of the game '''
        print 'Mancala Status\n'
        print ('Store B     B6   B5   B4   B3   B2   B1      Store A\n'
               '   {}        {}    {}    {}    {}    {}    {}        {}\n'
               '            {}    {}    {}    {}    {}    {}\n'
               '            A1   A2   A3   A4   A5   A6\n\n'.format(
                self._player_B_store, 
                self._pits[11], 
                self._pits[10], 
                self._pits[9], 
                self._pits[8], 
                self._pits[7], 
                self._pits[6], 
                self._player_A_store,
                self._pits[0],
                self._pits[1],
                self._pits[2],
                self._pits[3],
                self._pits[4],
                self._pits[5]))





def shell_cmd(cmd):
    ''' run a shell command '''
    try:
        return subprocess.Popen(cmd, stdin=None,
                                stdout=subprocess.PIPE,
                                stderr=None, shell=True).communicate()[0].strip()
    except subprocess.CalledProcessError:
        print "Unexpected error:", sys.exc_info()





if __name__ == '__main__':
    print main()

