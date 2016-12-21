# Solution to Project Euler Problem 13
# https://projecteuler.net/problem=13

# Work out the first ten digits of the sum of N 50-digit numbers.


#!/bin/python3

import sys

def euler13 (nums):
    sum = 0
    for n in nums:
        sum += int(str(n)[:15])
    return int(str(sum)[:10])

n = int(input())
nums = []
for _ in range(n):
    nums.append(input())

print(euler13(nums))

#> 5537376230
