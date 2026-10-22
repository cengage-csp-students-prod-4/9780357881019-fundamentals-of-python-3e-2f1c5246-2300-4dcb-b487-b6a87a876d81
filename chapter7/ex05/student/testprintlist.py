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

'''
Seperate code to actually test the printAll() function:
(Not accepted by grader)


def main():
    _table = ["elem1", "elem2", 3, 4, 5.0, 3+3]
    _tuple = (3+3, 5.0, 4, 3, "elem2", "elem1")
    _string = "elem1 elem2 3 4 5.0 3+3"
    _empty = []
    _bigList = []
    for x in range(500, 0, -1):
        _bigList.append(x)
    seq = None
    seqType = input(
    """Pick which sequence to list
    1 - Table
    2 - Tuple
    3 - String
    4 - Empty Table
    5 - Big List
    ---> """)
    if seqType == "1":
        seq = _table
    elif seqType == "2":
        seq = _tuple
    elif seqType == "3":
        seq = _string
    elif seqType == "4":
        seq = _empty
    elif seqType == "5":
        seq = _bigList

    printAll(seq)


def printAll(seq):
    print(
        "---------------------------------------\n", \
        "The current sequence: ", seq, \
        "\n---------------------------------------"
    )
    if seq:
        print(seq[0])
        printAll(seq[1:])

if __name__ == "__main__":
    main()
'''