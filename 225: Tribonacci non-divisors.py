def getM(a, b, c, divisor):

    l, m, k = b, c, (a + b + c) % divisor

    while (k and (l != a or m != b or k != c)):
        l, m, k = m, k, (l + m + k) % divisor
    return k

a, b, c, num = list(map(int,input().split(' ')))
n = 1
divisors = set([])
while num:
    n += 2
    for i in divisors:
        if not n % i:
            num -= 1
            break
    else:
        aa, bb, cc = a%n, b%n, c%n
        if (aa*bb*cc and getM(aa, bb, cc, n)):
            num -= 1
            divisors.add(n)

print(n)
