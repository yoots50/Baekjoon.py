def main():
    N, M = map(int, input().split())
    arr1 = [[0 for i in range(0, M)] for i in range(0, N)]
    arr2 = [[0 for i in range(0, M)] for i in range(0, N)]
    for i in range(0, N):
        arr1[i] = list(map(int, input().split()))
    for i in range(0, N):
        arr2[i] = list(map(int, input().split()))
    for i in range(0, N):
        for j in range(0, M):
            print(f"{arr1[i][j] + arr2[i][j]}", end = " ")
        print("")
main()