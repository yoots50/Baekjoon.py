def func(x, y):
    temp = x
    ret = 0
    while temp % y == 0:
        temp = temp // y
        ret += 1
    return ret


def main():
    N = int(input())
    twos = 0
    fives = 0
    for i in range(1, N + 1):
        if (i % 2) == 0:
            twos += func(i, 2)
        if (i % 5) == 0:
            fives += func(i, 5)
    ans = min(twos, fives)
    print(ans)


if __name__ == "__main__":
    main()