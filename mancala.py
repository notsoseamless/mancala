'''
Python implementation of Mancala
'''

import re
import os
import time
import sys
import subprocess


# constants
PIT_MAX = 6


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
    m.play()
    m.dump_status()



# http://www.pressmantoy.com/game-rules/Mancala_rules.pdf
# http://www.ultraboardgames.com/mancala/game-rules.php

class Mancala(object):
    ''' mancala container '''
    def __init__(self, name):
        ''' constructor '''
        self._pit_a = [4, 4, 4, 4, 4, 4]
        self._pit_b = [4, 4, 4, 4, 4, 4]
        self._store_a = 0
        self._store_b = 0

    def play(self):
        ''' play  the game '''
        print('Which pit (1 to 6)?')
        self.process_input(self.validate(1, 6, (int(raw_input('Input:')))))
        
    def process_input(self, pit):
        ''' process '''
        index = pit-1
        hand = 0
        # empty first pit
        hand = hand + self._pit_a[index]
        self._pit_a[index] = 0
        # add to own pits
        index += 1
        while hand > 0 and index < PIT_MAX:
            hand, self._pit_a[index] = self.transfer(hand, self._pit_a[index])
            index += 1
        # add to own store
        if hand > 0:
            hand, self._store_a = self.transfer(hand, self._store_a)
        # add to opps store
        index = 0
        while hand > 0 and index < PIT_MAX:
            hand, self._pit_b[index] = self.transfer(hand, self._pit_b[index])
            index += 1

    def transfer(self, a, b):
        ''' returm a tuple, transfering 1 from a to b '''
        if a > 0:
            a -= 1
            b += 1
        return a, b

    def validate(self, min, max, value):
        ''' check range of user input '''
        if min > value:
            return min
        elif max < value:
            return max
        else:
            return value
        


    def dump_status(self):
        ''' outputs text status of the game '''
        print '\n\nMancala Status\n'
        print ('                  B6   B5   B4   B3   B2   B1\n'
               'Store B           {}    {}    {}    {}    {}    {}        Store A\n'
               '   {}              {}    {}    {}    {}    {}    {}           {}\n'
               '                  A1   A2   A3   A4   A5   A6\n\n'.format(
                self._pit_b[5], 
                self._pit_b[4], 
                self._pit_b[3], 
                self._pit_b[2], 
                self._pit_b[1], 
                self._pit_b[0], 
                self._store_b, 
                self._pit_a[0],
                self._pit_a[1],
                self._pit_a[2],
                self._pit_a[3],
                self._pit_a[4],
                self._pit_a[5],
                self._store_a))




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

