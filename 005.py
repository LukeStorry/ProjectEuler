# Solution to Project Euler Problem 5
# https://projecteuler.net/problem=5

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(x,y):
    while y > 0:
        x, y = y, x%y
    return x

def lcm(a,b):
    return a * b // gcd(a,b)

def smallest_multiple(n):
    m = 1
    for i in range(1,n+1):
        m = lcm(m,i)
    return m
    
