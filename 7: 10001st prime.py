#!/bin/python3

import sys

def simp(n):
    lst = [2]
    if n == 1:
        return lst
    test_n = lst[-1] + 1
    while True:
        for j in lst:
            if j * j - 1 > test_n:
                lst.append(test_n)
                break
            if test_n % j == 0:
                break
        else:
            lst.append(test_n)
        test_n += 1
        if len(lst) == n:
            break

    return lst

l = simp(10000)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(l[n-1])
