def main():
    arr = list(map(int, input().split()))
    pieces = [1, 1, 2, 2, 2, 8]

    for i in range(6):
        print(pieces[i] - arr[i], end = " ")
    
main()
