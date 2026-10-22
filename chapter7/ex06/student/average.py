"""
Program: average.py
Author: Michael Guillen

Read from a given file and calculate the average of the numbers in given file
"""

import os, os.path
from functools import reduce

def main():
    fileName = input("Enter the input file name: ")
    numFile = open(os.getcwd() + os.sep + fileName)
    numTable = numFile.read()
    numFile.close()

    _sum, numCount = getNumbers(numTable)
    print("The average is", average(_sum, numCount))


def getNumbers(_list):
    splitList = _list.split()
    intList = list(map(lambda _str: int(_str), splitList))
    numCount = len(intList)
    numSum = reduce(lambda _sum, curNum: _sum + curNum, intList)

    return numSum, numCount

def average(_sum, numCount):
    avg = _sum / numCount

    return avg

if __name__ == "__main__":
    main()