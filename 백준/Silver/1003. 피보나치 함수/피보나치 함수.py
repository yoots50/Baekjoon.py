def fibo(n):
    if (n == 0):
        return [1, 0]
    elif (n == 1):
        return [0, 1]
    elif (memo[n] != [-1, -1]):
        return memo[n]
    memo[n] = [fibo(n - 1)[0] + fibo(n - 2)[0], fibo(n - 1)[1] + fibo(n - 2)[1]]
    return memo[n]

T = int(input())

for _ in range(T):
    N = int(input())
    memo = [[-1, -1] for _ in range(N + 1)]
    ptn = fibo(N)
    print(ptn[0], ptn[1])