def main():
    arr = []
    for i in range(10):
        arr.append(int(input()) % 42)
    arrSet = set(arr)
    print(len(arrSet))

main()