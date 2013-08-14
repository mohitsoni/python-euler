#!/usr/bin/env python

'''
For a mxn grid, number of paths equals: (m+n)C(m)
'''

m = 2
n = 2

grid = [[0 for j in range(n+1)] for i in range(m+1)]

def printGrid(grid):
    for row in grid:
        print row
    print

def countPaths(grid, i, j, val):
    printGrid(grid)
    grid[i][j] += val
    # Go right
    if j+1 < len(grid):
        countPaths(grid, i, j+1, grid[i][j])
    # Go down
    if i+1 < len(grid):
        countPaths(grid, i+1, j, grid[i][j])

def countPathsI(grid):
    i, j = 0, 0
    val = 1

    while True:
        grid[i][j] += val
        # Go right
        grid[i+1][j] += grid[i][j]
        # Go down
        grid[i][j+1] += grid[i][j]
        i = i+1
        j = j+1
        
        printGrid(grid)

print countPaths(grid,0,0,1)
