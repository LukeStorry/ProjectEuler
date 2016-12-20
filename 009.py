# Solution to Project Euler Problem 9
# https://projecteuler.net/problem=9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc

#!/bin/python3

import sys

def abc(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if c > 0 and c*c == a*a + b*b:
                return a*b*c
    return -1

#assert abc(12) == 60
#assert abc(4) == -1

print (abc(1000))
#> 31875000
