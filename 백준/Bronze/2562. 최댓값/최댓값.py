def main():
    arr = [0 for i in range(9)]
    for i in range(9):
        arr[i] = int(input())
    arrMAX = max(arr)
    print(arrMAX)
    print(arr.index(arrMAX) + 1)
main()
