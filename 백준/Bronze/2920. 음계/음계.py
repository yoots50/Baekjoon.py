def main():
    arr = list(map(int, input().split()))
    if (arr == sorted(arr)):
        print("ascending")
    elif (arr == sorted(arr)[::-1]):
        print("descending")
    else:
        print("mixed")
        
main()
