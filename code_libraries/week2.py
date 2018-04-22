from week1 import *
import re


def pat_count(pattern):
    pat = re.compile(pattern)
    
    def the_counter(tweet):
        pat_count = len(re.findall(pat,tweet))
        return pat_count
    
    return the_counter  # returns a function as a value