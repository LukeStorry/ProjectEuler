# Solution to Project Euler Problem 14
# https://projecteuler.net/problem=14

# Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?


import sys

# for memoization
# (next_val, steps_to_0)
arr = [(0,0),(0,0),(1,1)]
        
import sys

# for memoization
# (next_val, steps_to_0)
arr = [(0,0),(0,0)]
        
def calc_cell(n):
    global arr
    if n >= len(arr):
        arr.extend([None]*(n + 1 - len(arr)))
    if arr[n] is None:
        next_val = n//2 if n%2==0 else 3*n+1
        arr[n] = (next_val, calc_cell(next_val)[1] + 1)
    return arr[n]

def euler14 (n):
    best_start = 0
    best_steps = 0
    for start in range(n+1):
        (_, steps) = calc_cell(start)
        if steps >= best_steps:
            best_start = start
            best_steps = steps
    return best_start
        
print(euler14(1000000))    
    
    
# HR input:
# t = int(input())
# cases = []
# for _ in range(t):
#     n = (int(input()))
#     print(euler14(n))

