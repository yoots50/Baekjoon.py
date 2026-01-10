def NQ(step):
    if step == -1:
        return 1
    ret = 0
    for i in range(N):
        if (
            not rows[i]
            and not diagonals2[i + step]
            and not diagonals1[step - i + N - 1]
        ):
            rows[i] = 1
            diagonals1[step - i + N - 1] = 1
            diagonals2[i + step] = 1
            ret += NQ(step - 1)
            rows[i] = 0
            diagonals1[step - i + N - 1] = 0
            diagonals2[i + step] = 0
    return ret


def main():
    global N
    N = int(input())
    global rows, diagonals1, diagonals2
    rows = [0 for _ in range(N)]
    diagonals1 = [0 for _ in range(2 * N - 1)]  # \
    diagonals2 = [0 for _ in range(2 * N - 1)]  # /
    print(NQ(N - 1))

if __name__ == "__main__":
    main()