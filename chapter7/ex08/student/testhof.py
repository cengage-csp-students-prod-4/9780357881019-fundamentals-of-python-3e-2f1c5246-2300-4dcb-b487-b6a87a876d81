"""
Program: testhof.py
Author: Michael Guillen

Tests myMap, myFilter, and myReduce from the hof module by
comparing their results to Python's map, filter, and reduce.
"""

from functools import reduce
from hof import myMap, myFilter, myReduce

def square(x):
    return x ** 2

def odd(x):
    return x % 2 == 1

def add(x, y):
    return x + y

def main():
    lyst = list(range(5))
    print("Argument list:  ", lyst)
    print("map with ** 2  :", list(map(square, lyst)))
    print("myMap with ** 2:", myMap(square, lyst))
    print("filter with odd  :", list(filter(odd, lyst)))
    print("myFilter with odd:", myFilter(odd, lyst))
    print("reduce with +   :", reduce(add, lyst))
    print("myReduce with + :", myReduce(add, lyst))

    lyst = [3]
    print("Argument list:  ", lyst)
    print("reduce with +   :", reduce(add, lyst))
    print("myReduce with + :", myReduce(add, lyst))

    # reduce needs a nonempty list, so only map and filter here
    lyst = []
    print("Argument list:  ", lyst)
    print("map with ** 2  :", list(map(square, lyst)))
    print("myMap with ** 2:", myMap(square, lyst))
    print("filter with odd  :", list(filter(odd, lyst)))
    print("myFilter with odd:", myFilter(odd, lyst))

if __name__ == "__main__":
    main()
