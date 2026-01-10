import sys

sys.setrecursionlimit(10**6)

def dp(N, prevColor):
    if N == -1:
        return 0
    if memo[N][prevColor] != -1:
        return memo[N][prevColor]
    ret = []
    for i in range(3):
        if i != prevColor:
            ret.append(dp(N - 1, i) + graph[N][i])
    memo[N][prevColor] = min(ret)
    return memo[N][prevColor]


def main():
    N = int(input())
    global graph
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i] = list(map(int, input().split()))
    global memo
    memo = [[-1 for _ in range(3)] for _ in range(N)]
    print(dp(N - 1, -1))


if __name__ == "__main__":
    main()