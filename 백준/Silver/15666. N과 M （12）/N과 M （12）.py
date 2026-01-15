import sys

sys.setrecursionlimit(10**6)


def dfs(p, start, status):
    if len(status) == M:
        for i in range(M):
            print(status[i], end="")
            if i != M - 1:
                print(" ", end="")
        print()
        return
    for i in range(start, N):
        status.append(p[i])
        dfs(p, i, status)
        status.pop()


def main():
    global N, M
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    p = set(p)
    p = list(p)
    N = len(p)
    p.sort()
    dfs(p, 0, [])


if __name__ == "__main__":
    main()
