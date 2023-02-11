N = int(input())
for _ in range(N):
    d, f, p = map(float, input().split())
    print("$%0.2f" % (d * f * p))