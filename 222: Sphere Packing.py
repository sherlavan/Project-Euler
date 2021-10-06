from math import sqrt, modf

Rpipe, nBall = list(map(int,input().split(' ')))
BallsRadius = list(sorted(map(float,input().split(' '))))
BallsRadius = list(map(lambda x : x*1000,BallsRadius))

Dpipe = Rpipe * 2000

if nBall < 2:
    print(round(BallsRadius[0]*2))
    
elif nBall ==2:
    c = BallsRadius[0] + BallsRadius[1]
    x = sqrt(c*c -(Dpipe - c)*(Dpipe - c))
    print(round((x + c)))
    
else:
    
    if len(BallsRadius)%2==1:
        permut = BallsRadius[::-2] + BallsRadius[1::2]
    else:
        permut = BallsRadius[::-2] + BallsRadius[0::2]
        
    m, l = modf(permut[0] + permut[-1])

    for i in range(len(permut) - 1):
        gip = permut[i] + permut[i + 1]
        tm ,x = modf(sqrt(gip * gip -(Dpipe - gip) * (Dpipe - gip)))
        l += x
        m += tm

    print(round(l + m))
