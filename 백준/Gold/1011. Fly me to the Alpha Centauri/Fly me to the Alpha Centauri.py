import math

T = int(input())

for i in range(0, T):
    x, y = map(int, input().split(' '))
    d = y - x
    maxdis = int(math.sqrt(d))
    if (int(math.sqrt(d)) == math.sqrt(d)):
        print(maxdis * 2 - 1)
    else:
        d -= (maxdis * (maxdis + 1)) - maxdis
        if (d < ((maxdis + 1)**2 - maxdis**2) / 2):
            print(maxdis * 2)
        else:
            print(maxdis * 2 + 1)