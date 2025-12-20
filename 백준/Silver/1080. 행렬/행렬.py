def invert(arr1, startX, startY):
    for i in range(3):
        for j in range(3):
            if arr1[startX + i][startY + j] == "0":
                arr1[startX + i][startY + j] = "1"
            else:
                arr1[startX + i][startY + j] = "0"


def gd(A, B, N, M):
    if N < 3 or M < 3:
        if (A == B):
            return 0
        return -1
    maxRow = N - 2
    maxCol = M - 2
    ret = 0
    for i in range(maxRow):
        for j in range(maxCol):
            if (j == maxCol - 1) and (not A[i][j : j + 3] == B[i][j : j + 3]):
                invert(A, i, j)
                if not (A[i][j : j + 3] == B[i][j : j + 3]):
                    return -1
                else:
                    ret += 1

            elif not (A[i][j] == B[i][j]):
                invert(A, i, j)
                ret += 1

    if not A == B:
        return -1

    return ret


def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


def main():
    N, M = map(int, input().split())  # N: R, M: C
    A = [[0 for _ in range(M)] for _ in range(N)]
    B = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        tmpString = input()
        for j in range(M):
            A[i][j] = tmpString[j]
    for i in range(N):
        tmpString = input()
        for j in range(M):
            B[i][j] = tmpString[j]
    print(gd(A, B, N, M))


if __name__ == "__main__":
    main()
