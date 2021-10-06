def sumstr(s :str):
    l = list(map(int,list(s)))
    return sum(l)
    
t = int(input())
for a000 in range(t):
    n = int(input())
    s=str(2<<n-1)
    print(sumstr(str(s)))
