"""
Program: hof.py
Author: Michael Guillen

Defines myMap, myFilter, and myReduce, our own versions of
Python's higher-order functions map, filter, and reduce.
"""

def myMap(function, lyst):
    """Returns a list of the results of applying function
    to each item in lyst."""
    results = []
    for item in lyst:
        results.append(function(item))
    return results

def myFilter(predicate, lyst):
    """Returns a list of the items in lyst for which
    predicate returns True."""
    results = []
    for item in lyst:
        if predicate(item):
            results.append(item)
    return results

def myReduce(function, lyst):
    """Applies function of two arguments cumulatively to the
    items in lyst (which must be nonempty) and returns the
    single value that results."""
    result = lyst[0]
    for item in lyst[1:]:
        result = function(result, item)
    return result
