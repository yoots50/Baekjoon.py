import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S = [[] for _ in range(N)]
    for i in range(N):
        S[i] = list(map(int, input().split()))
        if i == 0:
            for j in range(N):
                if j == 0:
                    continue
                S[i][j] += S[i][j - 1]
        else:
            for j in range(N):
                if j == 0:
                    S[i][j] += S[i - 1][j]
                else:
                    S[i][j] += S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans = S[x2 - 1][y2 - 1]
        if x1 >= 2:
            ans -= S[x1 - 2][y2 - 1]
        if y1 >= 2:
            ans -= S[x2 - 1][y1 - 2]
        if (x1 >= 2) and (y1 >= 2):
            ans += S[x1 - 2][y1 - 2]
        print(ans)


if __name__ == "__main__":
    main()
