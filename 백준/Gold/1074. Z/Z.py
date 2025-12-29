def recursion(N, r, c):
    if N == 1:
        return r * 2 + c
    qs = 4 ** (N - 1)
    b = 2 ** (N - 1)
    if r < b and c < b:
        return recursion(N - 1, r, c)
    elif r < b and c >= b:
        return recursion(N - 1, r, c - b) + qs
    elif r >= b and c < b:
        return recursion(N - 1, r - b, c) + 2 * qs
    else:
        return recursion(N - 1, r - b, c - b) + 3 * qs


def main():
    N, r, c = map(int, input().split())
    print(recursion(N, r, c))


if __name__ == "__main__":
    main()