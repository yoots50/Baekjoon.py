def main():
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(3)

    else:
        memo = [-1 for _ in range(n + 1)]
        memo[1] = 1
        memo[2] = 3
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] * 2
        print(memo[n] % 10007)


if __name__ == "__main__":
    main()
