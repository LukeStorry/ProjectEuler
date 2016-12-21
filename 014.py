# Solution to Project Euler Problem 14
# https://projecteuler.net/problem=14

# Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?

import sys

# varies by system - memory causes segfaults
limit = 100000000

# for memoization
arr_next = [1, 1, 1] + [0]*limit
arr_dist = [0, 0, 1] + [0]*limit
        
def calc_cell(n):
    global arr_next, arr_dist
    if n >= len(arr_next):
        print("Error: n=" +str(n))
        exit()
    if arr_next[n] == 0:
        next_val = n//2 if n%2==0 else 3*n+1
        arr_next[n] = next_val
        arr_dist[n] = calc_cell(next_val)[1] + 1
    return (arr_next[n], arr_dist[n])

def euler14 (n):
    best_start = 0
    best_steps = 0
    for start in range(n+1):
        (_, steps) = calc_cell(start)
        if steps >= best_steps:
            best_start = start
            best_steps = steps
    return best_start

#Due to memory limits, max 25000
print(euler14(25000))
#> 23529

    
    
# HR input:
# t = int(input())d
# cases = []
# for _ in range(t):
#     n = (int(input()))
#     print(euler14(n))

