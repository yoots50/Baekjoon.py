def dp(N):
    if N == 1:
        return 0
    if N == 2 or N == 3:
        return 1
    comp = []
    if memo[N] is not -1:
        return memo[N]
    comp.append(dp((N - (N % 3)) // 3) + N % 3 + 1)
    comp.append(dp((N - (N % 2)) // 2) + N % 2 + 1)
    memo[N] = min(comp)
    return memo[N]


def main():
    N = int(input())
    global memo
    memo = [-1] * (N + 1)
    print(dp(N))


if __name__ == "__main__":
    main()