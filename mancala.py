'''
Python implementation of Mancala
'''

import re
import os
import time
import sys
import subprocess


# constants


def timing_function_decorator(timed_function):
    ''' Outputs time a function takes to execute '''
    def wrapper():
        ''' wrapper '''
        t_start = time.time()
        timed_function()
        t_end = time.time()
        return "Script ran for " + str((t_end - t_start)) + " seconds\n"
    return wrapper


@timing_function_decorator
def main():
    ''' main function '''
    m = Mancala('M')





class Mancala(object):
    ''' mancala container '''
    def __init__(self, name):
        ''' constructor '''
        print 'created' 







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

