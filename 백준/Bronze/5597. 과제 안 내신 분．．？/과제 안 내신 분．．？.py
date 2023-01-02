def main():
    arr = set()
    arr30 = {i for i in range(1, 31)}
    for i in range(0, 28):
        arr.add(int(input()))
    answer = sorted(arr30 - arr)
    print(answer[0])
    print(answer[1])
main()