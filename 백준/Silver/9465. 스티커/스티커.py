import sys

NONE = -1
UP = 0
DOWN = 1

sys.setrecursionlimit(10**6)


def dp(start, prevPos):
    if start >= n:
        return 0
    ret = []
    if prevPos == NONE:
        return max(
            dp(start + 1, UP) + score[UP][start],
            dp(start + 1, DOWN) + score[DOWN][start],
        )
    elif memo[start][prevPos] != -1:
        return memo[start][prevPos]
    elif prevPos == UP:
        ret = [dp(start + 1, DOWN) + score[DOWN][start]]
        if start + 1 < n:
            ret.append(dp(start + 2, DOWN) + score[DOWN][start + 1])
        memo[start][prevPos] = max(ret)
        return memo[start][prevPos]
    elif prevPos == DOWN:
        ret = [dp(start + 1, UP) + score[UP][start]]
        if start + 1 < n:
            ret.append(dp(start + 2, UP) + score[UP][start + 1])
        memo[start][prevPos] = max(ret)
        return memo[start][prevPos]


def main():
    T = int(input())
    for _ in range(T):
        global n
        n = int(input())
        global score
        score = []
        for _ in range(2):
            score.append(list(map(int, input().split())))
        global memo
        memo = [[-1 for _ in range(2)] for _ in range(n)]
        print(dp(0, NONE))


if __name__ == "__main__":
    main()
