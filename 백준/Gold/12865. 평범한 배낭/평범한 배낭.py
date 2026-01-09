def dp(N, K):
    if N == 0:
        if K >= weights[N]:
            return values[N]
        return 0
    if memo[N][K] != -1:
        return memo[N][K]
    if K >= weights[N]:
        memo[N][K] = max(dp(N - 1, K - weights[N]) + values[N], dp(N - 1, K))
        return memo[N][K]
    memo[N][K] = dp(N - 1, K)
    return memo[N][K]


def main():
    N, K = map(int, input().split())
    global values, weights
    values = []
    weights = []
    for i in range(N):
        W, V = map(int, input().split())
        values.append(V)
        weights.append(W)
        global memo
    memo = [[-1 for i in range(K + 1)] for i in range(N)]
    print(dp(N - 1, K))


if __name__ == "__main__":
    main()
