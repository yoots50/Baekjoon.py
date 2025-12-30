def printer(arr):
    print("[", end="")
    for i in range(len(arr)):
        print(arr[i], end="")
        if i != len(arr) - 1:
            print(",", end="")
    print("]")


def main():
    T = int(input())
    for _ in range(T):
        p = input()
        n = int(input())
        arr = input()[1:-1].split(",")
        if arr[0] == "":
            arr = []
        isReversed = False
        startIdx = 0
        endIdx = len(arr)
        isError = False
        for i in range(len(p)):
            if p[i] == "R":
                isReversed = not isReversed
            else:
                if isReversed:
                    endIdx -= 1
                else:
                    startIdx += 1
                if endIdx < startIdx:
                    isError = True
                    break
        if isError:
            print("error")
        else:
            if isReversed:
                printer(arr[startIdx:endIdx][::-1])
            else:
                printer(arr[startIdx:endIdx])


if __name__ == "__main__":
    main()