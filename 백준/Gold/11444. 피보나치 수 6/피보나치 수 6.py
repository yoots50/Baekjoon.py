def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        if n in memo:
            return memo[n]
        elif n % 2 == 0:
            memo[n] = (
                (fibo(n // 2) % 1000000007)
                * (fibo(n // 2 + 1) % 1000000007 + fibo(n // 2 - 1) % 1000000007)
                % 1000000007
            ) % 1000000007
        else:
            l = fibo((n + 1) // 2) % 1000000007
            r = fibo((n - 1) // 2) % 1000000007
            memo[n] = ((l * l) % 1000000007 + (r * r) % 1000000007) % 1000000007
        return memo[n]


def main():
    n = int(input())
    global memo
    memo = {}
    print(fibo(n))


if __name__ == "__main__":
    main()
