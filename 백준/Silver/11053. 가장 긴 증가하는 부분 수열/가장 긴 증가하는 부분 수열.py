def main():
    N = int(input())
    A = list(map(int, input().split()))
    memo = [-1 for _ in range(N)]
    memo[N - 1] = 1
    for i in range(N - 1, -1, -1):
        maxt = 0
        for j in range(i + 1, N):
            if A[i] < A[j] and memo[j] != -1:
                if memo[j] > maxt:
                    maxt = memo[j]
            memo[i] = maxt + 1
    print(max(memo))


if __name__ == "__main__":
    main()
