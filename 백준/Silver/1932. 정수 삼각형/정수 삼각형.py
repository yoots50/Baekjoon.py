def dp(x, y):
    if x == n - 1:
        return tr[x][y]
    if memo[x][y] != -1:
        return memo[x][y]
    memo[x][y] = max(dp(x + 1, y) + tr[x][y], dp(x + 1, y + 1) + tr[x][y])
    return memo[x][y]


def main():
    global n
    n = int(input())
    global tr
    tr = [[] for _ in range(n)]
    for i in range(n):
        tr[i] = list(map(int, input().split()))
    global memo
    memo = [[-1 for _ in range(i + 1)] for i in range(n)]
    print(dp(0, 0))


if __name__ == "__main__":
    main()
