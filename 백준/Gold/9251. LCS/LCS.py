import sys

sys.setrecursionlimit(10**6)

def dp(la, lb):
    if la == -1 or lb == -1:
        return 0
    if memo[la][lb] != -1:
        return memo[la][lb]
    if A[la] == B[lb]:
        memo[la][lb] = dp(la - 1, lb - 1) + 1
    else:
        memo[la][lb] = max(dp(la - 1, lb), dp(la, lb - 1))
    return memo[la][lb]


def main():
    global A, B
    A = input()
    B = input()
    global memo
    memo = [[-1 for _ in range(len(B))] for _ in range(len(A))]
    print(dp(len(A) - 1, len(B) - 1))


if __name__ == "__main__":
    main()