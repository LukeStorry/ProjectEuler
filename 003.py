#Solution to Project Euler Problem 2
#https://projecteuler.net/problem=2
#What is the largest prime factor of the number 600851475143?

from math import sqrt
def largest_prime_factor(n):
    for i in range (2, int(sqrt(n))+1):
        while n % i == 0:
            n //= i
        if n == 1:
            return i
    return n
        
        
assert largest_prime_factor(2) == 2
assert largest_prime_factor(10) == 5
assert largest_prime_factor(17) == 17


print (largest_prime_factor(600851475143))
#> 6857
