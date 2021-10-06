#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m = int(n**0.5) + 1
    s = 1
    for i in range(2, m):
        while n % i == 0:
            n //= i
            s = i
    if n > s:
        print(n)
    else:
        print(s)
