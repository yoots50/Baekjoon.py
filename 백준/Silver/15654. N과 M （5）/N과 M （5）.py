def printArr(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
        if i != len(arr) - 1:
            print(" ", end="")
    print()


def bt(prev, N, M, buf):
    if M == 0:
        printArr(buf)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            buf.append(arr[i])
            bt(i, N, M - 1, buf)
            buf.pop()
            visited[i] = 0


def main():
    N, M = map(int, input().split())
    global arr
    arr = list(map(int, input().split()))
    global visited
    visited = [0] * N
    arr.sort()
    bt(-1, N, M, [])


if __name__ == "__main__":
    main()
