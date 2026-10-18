"""
Program: stats.py
9-24-2026
Michael Guillen

Declare the mean, median, and mode functions for a given list
"""

def main():
    myList = [7,2,9,3,1,4]
    myList.sort()

    print(mean(myList))
    print(median(myList))
    print(mode(myList))


def mean(list):
    """finds the mean of a list"""
    sum = int()
    for num in list:
        sum += num

    return sum / len(list)

def median(list):
    """finds the median of a list"""
    middle = 0

    if len(list) % 2 == 1:
        middle = list[len(list) // 2]
    else:
        middle = (list[len(list) // 2] + list[(len(list) // 2) + 1]) / 2

    return middle

def mode(list):
    """finds the mode(s), if any, of a list"""
    dict = {}
    for index in list:
        num = dict.get(index)
        if num is None:
            dict[index] = 1
        else:
            dict[index] = num + 1
    
main()