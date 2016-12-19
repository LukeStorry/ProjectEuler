# Solution to Project Euler Problem 6
# https://projecteuler.net/problem=6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(n):
    return ((n * (n + 1)) // 2)**2 - (n * (n + 1) * (2 * n + 1)) // 6

assert sum_square_difference(10) == 2640

     

#> 25164150
