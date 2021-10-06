#!/bin/python3

import sys
'''
a=[3,5]
n=N-1//a
(2a+(n-1)d)*n/2
d=a
a(n+1)n/2
'''

def count_sum(n:int):
    s = 0
    for a in [3, 5]:
        nx = (n - 1)//a
        sx = (a * (nx + 1) * nx)>>1
        s += sx
    nx = (n - 1)//15
    sx = (15 * (nx + 1) * nx)>>1
    s -= sx
    return s

N=[]
tests = int(input().strip())
for _ in range(tests):
    N.append(int(input().strip()))
for n in N:
    print(count_sum(n))
