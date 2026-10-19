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
            print("The program's estimate is ", newton(int(_input)))
            print("Python's estimate is ", math.sqrt(int(_input)))

def newton(x, est = 1.0):
    tol = 0.0000001
    est = (est + x / est) / 2
    diff = abs(x - est ** 2)
    if diff >= tol:
        return newton(x, est)
    else:
        return est

main()