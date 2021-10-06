#!/bin/python3

import sys

p1 = []
for a in range(4, 3000, 4):
    for b in range (3, 3000):
         if a + b >2999: break
         c2 = a**2 + b**2
         c = c2**0.5
         if a + b + c > 3000: break
         if c == int(c):
            p1.append([a,b,int(c)])
p =p1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = -1
    pp = list(filter(lambda x: sum(x)==n, p))
    for ppp in pp:
        t = ppp[0]*ppp[1]*ppp[2]
        if res< t: res = t
    print(res)
