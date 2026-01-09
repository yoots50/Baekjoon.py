def printArr(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
        if i != len(arr) - 1:
            print(" ", end="")
    print()


def bt(now, N, M, arr):
    if M == 0:
        printArr(arr)
        return
    for i in range(now, N + 1):
        arr.append(i)
        bt(i, N, M - 1, arr)
        arr.pop()


def main():
    N, M = map(int, input().split())
    bt(1, N, M, [])


if __name__ == "__main__":
    main()
