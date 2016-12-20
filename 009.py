# Solution to Project Euler Problem 9
# https://projecteuler.net/problem=9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc

#!/bin/python3

import sys

def abc(n):
    results = [-1]
    for a in range(n):
        b = (a*a-(a-n)*(a-n))//(2*(a-n))
        c = n - a - b
        if a > 0 and b > 0 and c > 0 and a*a + b*b == c*c:
            results.append(a*b*c)
    return sorted(results)[-1]

#assert abc(12) == 60
#assert abc(4) == -1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(abc(n))

print (abc(1000))
#> 31875000
