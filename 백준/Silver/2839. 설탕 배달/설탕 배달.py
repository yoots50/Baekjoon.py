import sys
sys.setrecursionlimit(10 ** 7)

memo = [0 for i in range(5002)]

def func(N):
    if (N == 3 or N == 5):
        return 1;
    if (N < 5):
        return 5001;
    if (memo[N] != 0):
        return memo[N]
    memo[N] = min(1 + func(N - 3), 1 + func(N - 5))
    return memo[N]

def main():
    N = int(input())
    answer = func(N)
    if (answer >= 5001):
        print('-1')
    else:
        print(answer)

main()