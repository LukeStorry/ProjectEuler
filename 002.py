#Solution to Project Euler Problem 2
#https://projecteuler.net/problem=2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def sum_even_fibs(n):
    a=1
    b=0
    sum = 0
    while a < n:
        if a%2==0: sum+=a
        (a,b) = (a+b,a)
    return sum

assert sum_even_fibs(2) == 0
assert sum_even_fibs(10) == 10
assert sum_even_fibs(100) == 44

print sum_even_fibs(4000000)
