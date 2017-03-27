#-------------------------------------------------------------------------------
# Name:        IS 602 Homework 6
# Purpose:     Sort and Search with NumPy
#
# Author:      OluwakemiOmotunde
#
# Created:     05/02/2017
# Copyright:   (c) OluwakemiOmotunde 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
setup = '''

import numpy as np
import copy
import numpy.random as npr
import random

#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    """Takes a list for input and returns a sorted version of the list with use of a loop.
    I was able to find a great tutorial on YouTube (https://www.youtube.com/watch?v=lEA31vHiry4) that walked me through insertion sort"""

    for index in range(1, len(input)):
        value = input[index]
        i = index - 1
        while i >= 0:
            if value < input[i]:
                input[i+1] = input[i]
                input[i] = value
                i = i-1
            else:
                    break
    return input


#with NumPy

def num_sort(input):
    np.sort(input)
    return input

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):
    """Takes a list and returns a sorted version of the list with use of a loop"""
    return sorted(input)#return a value, I tried this with return (input.sort) and it did not work

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    """"Take a list and returns true if a value is in the list. It returns false otherwise."""
    while value in input:
            return "True"
    else:
           return "False"


#with NumPy

def num_search(input, value):
    loc = np.where(input == value)
    return len(loc)

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    if value in input:
        return "True"
    else:
        return "False"
#We will now generate the arrays to test the functions

array = np.random.permutation(np.arange(10000))[:]
my_list = array.tolist()

#to pick a random number between 1 and 500 we use

ran_num = random.randrange(1, 500)
'''

#now to test the time of each function
import timeit


if __name__ == "__main__":

    n = 10000

    time = timeit.Timer("x = copy.copy(my_list); sortwithloops(x)", setup)
    print "Sort with loops takes:", time.timeit(n), "seconds"

    time = timeit.Timer("x = copy.copy(my_list); sortwithoutloops(x)", setup)
    print "Sort without loops takes:", time.timeit(n), "seconds"

    time = timeit.Timer("x = copy.copy(array); num_sort(x)", setup)
    print "Sort with NumPy takes:", time.timeit(n), "seconds"

    time = timeit.Timer("x = copy.copy(my_list); y = copy.copy(ran_num); searchwithloops(x, y)", setup)
    print "Search with loops takes:", time.timeit(n), "seconds"

    time = timeit.Timer("x = copy.copy(my_list); y = copy.copy(ran_num); searchwithoutloops(x, y)", setup)
    print "Search without loops takes:", time.timeit(n), "seconds"

    time = timeit.Timer("x = copy.copy(array); y = copy.copy(ran_num); num_search(x, y)", setup)
    print "Search with NumPy takes:", time.timeit(n), "seconds"

