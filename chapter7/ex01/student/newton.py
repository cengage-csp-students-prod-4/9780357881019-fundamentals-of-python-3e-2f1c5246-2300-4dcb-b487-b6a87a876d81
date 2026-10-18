"""
Program: newton.py
Michael G.

A program to approximate square roots using a recursive function
"""
import math

def main():
    while True:
        _input = int(input("Enter a positive number or enter/return to quit: "))
        if _input == "":
            break
        print("The program's estimate is ", newton(_input))
        print("Python's estimate is ", math.sqrt(_input))

def newton(x):
    est = 1.0
    