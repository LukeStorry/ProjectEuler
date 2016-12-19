#Solution to Project Euler Problem 2
#https://projecteuler.net/problem=2
#What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
    for i in range (2, n):
        while n % i==0:
            n //= i
        if n == 1:
            return i
