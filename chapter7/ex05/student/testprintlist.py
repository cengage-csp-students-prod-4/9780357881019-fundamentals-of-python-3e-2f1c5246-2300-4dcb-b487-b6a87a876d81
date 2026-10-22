"""
Program: testprintlist.py
Author: Michael Guillen

A program to test Lee's 'printList()' function
"""

def main():
    _string = "elem1 elem2 3 4 5.0 3+3"
    printAll(_string)


def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])

if __name__ == "__main__":
    main()