# Solution to Project Euler Problem 11
# https://projecteuler.net/problem=11
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
#!/bin/python3

#!/bin/python3

import sys

height = 20
width = 20
adj = 4

grid = []
for _ in range(height):
   row = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(row)

def product(list):
    p = 1
    for i in list:
        p *= i
    return p
    
def down (row, col):
    rows = [(row+x) % height for x in range(adj)]
    vals = [grid[r][col] for r in rows]
    return product(vals)

def right (row, col):
    cols = [(col+x) % width for x in range(adj)]
    vals = [grid[row][c] for c in cols]
    return product(vals)

def downright (row, col):
    rows = [(row+x) % height for x in range(adj)]
    cols = [(col+x) % width for x in range(adj)]
    vals = [grid[rows[i]][cols[i]] for i in range(adj)]
    return product(vals)
    
def downleft (row, col):
    rows = [(row+x) % height for x in range(adj)]
    cols = [(col-x) % width for x in range(adj)]
    vals = [grid[rows[i]][cols[i]] for i in range(adj)]
    return product(vals)
    
    
best = 0
for row in range (height):
    for col in range(width):
        this = max(down(row, col), right(row, col), downright(row, col), downleft(row, col))
        if this > best:
            best = this
            
print(best)
    

#> 70600674
    
