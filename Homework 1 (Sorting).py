#-------------------------------------------------------------------------------
# Name:        Homework 1
# Purpose:
#
# Author:      OluwakemiOmotunde
#
# Created:     05/02/2017
# Copyright:   (c) OluwakemiOmotunde 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    if value in input:
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
