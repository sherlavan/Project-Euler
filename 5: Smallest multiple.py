#!/bin/python3

import sys
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nok = 1
    while True:
        for i in range(1, n + 1):
            if nok % i == 0:
                continue
            else:
                nok += 1
                break
        else:
            print(nok)
            break
