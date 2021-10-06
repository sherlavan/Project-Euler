#!/bin/python3

import sys

def build_poli():
    lst = []
    for i in range(999, 110, -1):
        for j in range(999, 110, -1):
            prod = i*j
            if check_poli(str(prod)):
                lst.append(prod)
            
    return lst

def check_poli(s: str):
    s1, s2 = s[:3],s[:2:-1]
    if s1 == s2:
        return True
    return False

p = build_poli()
poli = sorted(set(p))
# print(poli)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(len(poli)):
        if poli[i]>=n:
            print(poli[i-1])
            break
