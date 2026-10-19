"""
Program: newton.py
Michael G.

A program to approximate square roots using a recursive function
"""
import math

def main():
    while True:
        _input = input("Enter a positive number or enter/return to quit: ")
        if _input == "":
            break
        else:
            print("The program's estimate is ", newton(float(_input)))
            print("Python's estimate is ", math.sqrt(float(_input)))

def improvedEstimate(x, est):
    est = (est + x / est) / 2
    return est

def limitReached(x, est, tol=0.000001):
    diff = abs(x - est ** 2)
    if diff >= tol:
        return False
    else:
        return True


def newton(x, est = 1.0):
    est = improvedEstimate(x, est)
    if limitReached(x, est) == False:
        return newton(x, est)
    else:
        return est

if __name__ == "__main__":
    main()
