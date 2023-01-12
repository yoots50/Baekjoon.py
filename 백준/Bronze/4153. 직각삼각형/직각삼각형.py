def main():
    while (True):
        arr = list(map(int, input().split()))
        if (sum(arr) == 0):
            break
        m = arr.pop(arr.index(max(arr)))
        if (m**2 == arr[0]**2 + arr[1]**2):
            print("right")
        else:
            print("wrong")
    
main()