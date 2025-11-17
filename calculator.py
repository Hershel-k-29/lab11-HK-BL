"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        raise ZeroDivisionError
    else:
        return a/b

def logarithm(a, b):
    if a<=1 or b <= 0:
        raise ValueError
    return math.log(b, a)# use math library/raise ValueError

def exponent(a, b):
    return a**b

