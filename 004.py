#Solution to Project Euler Problem 4
#https://projecteuler.net/problem=4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Extra from HackerRank: Find the largest palindrome made from the product of two 3-digit numbers which is less than N.



def is_palindrome(n):
    return str(n) == str(n)[::-1]

assert is_palindrome(1)
assert not is_palindrome(10)
assert is_palindrome(101)


def largest_product_palindrome_less_than(n):
    limit = int('9'*(len(str(n))//2))
    best = 0
    for i in range(limit):
        for j in range(limit):
            current = i*j
            if current > n:
                return best
            if is_palindrome(current):
                best = current
            
