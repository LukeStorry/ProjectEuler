#Solution to Project Euler Problem 1
#https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiple(n, m):
    multiples = (n-1)//m
    return m*(multiples*(multiples+1)//2)

def sum_of_multiples(n):
    return  sum_multiple(n,3) + sum_multiple(n,5) - sum_multiple(n,15)
    
    
 
assert sum_of_multiples(10) == 23
assert sum_of_multiples(100) == 2318


print(sum_of_multiples(1000))
