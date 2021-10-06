#!/bin/python3

import sys

def po(l):
    r = 1
    for a in l:
        r *= a
    return r

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
p = 0
# gor
for i in range(20):
    for j in range(17):
        t = po(grid[i][j:j+4])
        if t > p: p = t
#vert
for i in range(20):
    for j in range(17):
        t = po([grid[j][i],grid[j+1][i],grid[j+2][i],grid[j+3][i]])
        if t > p: p = t            

# dia
for k in range(17):
    for i in range(3,20):
        l = []
        for j in range(4):
            l.append(grid[k + j][i - j])
        t = po(l)
        if t > p: p = t

# cross dia
for k in range(17):
    for i in range(17):
        l = []
        for j in range(4):
            l.append(grid[k + j][i + j])
        t = po(l)
        if t > p: p = t    

print(p)
