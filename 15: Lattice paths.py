n = 501
m = 501
lst = [[1,1]]
for i in range(1, n + m):
    lst.append([1] * (i + 2))
    for j in range(1, i + 1):
        lst[i][j] =  lst[i - 1][j - 1] + lst[i - 1][j]

t = int(input().strip())
for a0 in range(t):
    n, m =list(map(int,input().strip().split(' ')))
    print(lst[n + m - 1][m] % (10**9 + 7))
