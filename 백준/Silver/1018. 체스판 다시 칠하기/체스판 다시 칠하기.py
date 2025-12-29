def main():
    N, M = map(int, input().split())
    board = [[] for _ in range(N)]
    for i in range(N):
        board[i] = input()

    ans = 10000000
    for row in range(N - 7):
        for col in range(M - 7):
            Wcnt = 0
            Bcnt = 0
            for i in range(row, row + 8):
                for j in range(col, col + 8):
                    if (i + j) % 2 == 0 and board[i][j] == "W":
                        Bcnt += 1
                    if (i + j) % 2 == 1 and board[i][j] == "B":
                        Bcnt += 1
                    if (i + j) % 2 == 1 and board[i][j] == "W":
                        Wcnt += 1
                    if (i + j) % 2 == 0 and board[i][j] == "B":
                        Wcnt += 1
            cnt = min(Wcnt, Bcnt)
            if cnt < ans:
                ans = cnt

    print(ans)


if __name__ == "__main__":
    main()