lst = []
N = int(input())
for a in range(N):
    t = input()
    shift = N // 10 + 1
    if shift >= 40:
        lst.append(int(t))
    else:
        lst.append(int(t[:10 + shift]))
astr = str(sum(lst))
print(astr[:10])
