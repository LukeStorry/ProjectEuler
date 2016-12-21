# Solution to Project Euler Problem 14
# https://projecteuler.net/problem=14

# Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?
import sys

#any higher and memory causes segfaults
limit = 10000000

# for memoization
arr_steps = [0, 0, 1] + [-1]*limit
        
def calc_dist(n):
    global arr_steps
    
    # ignore things above limit
    if n > limit:
        return 1
    
    # if no value yet, calculate it
    if arr_steps[n] == -1:
        next_val = n//2 if n%2==0 else 3*n+1
        arr_steps[n] = calc_dist(next_val) + 1
        
    return arr_steps[n]

def euler14 (n):
    best_start = 0
    best_steps = 0
    for start in range(n+1):
        steps = calc_dist(start)
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

