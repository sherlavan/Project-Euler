#!/bin/python3

import sys
def ss(s):
    r = 1
    for i in range(len(s)):
        r *= int(s[i])
    return r

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    s = n - k
    a = []
    for i in range(s + 1):
        a.append(ss(num[i:i+k]))
    print(max(a))
    
