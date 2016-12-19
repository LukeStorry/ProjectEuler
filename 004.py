#Solution to Project Euler Problem 4
#https://projecteuler.net/problem=4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Extra from HackerRank: Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
#I extended this further to allow a digits parameter, d


def largest_product_palindrome_less_than(d,n):
    limit = int('9'*d)
    best = 0
    for i in range(limit):
        for j in range(1,i+1):
            current = i*j
            if current >= n:
                break
            if current > best and is_palindrome(current):
                best = current
    return best


assert largest_product_palindrome_less_than(1, 10) == 9
assert largest_product_palindrome_less_than(2, 10) == 9
assert largest_product_palindrome_less_than(1, 100) == 9
assert largest_product_palindrome_less_than(2, 100) == 99

assert largest_product_palindrome_less_than(3, 101110) == 101101
assert largest_product_palindrome_less_than(3, 800000) == 793397

print(largest_product_palindrome_less_than(3,9999999))

#> 993 * 913 = 906609
