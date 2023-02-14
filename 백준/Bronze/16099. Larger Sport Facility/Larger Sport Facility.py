N = int(input())
for _ in range(N):
    lt, wt, le, we = map(int, input().split())
    E = le * we
    T = lt * wt
    if (E > T):
        print("Eurecom")
    elif (E < T):
        print("TelecomParisTech")
    else:
        print("Tie")