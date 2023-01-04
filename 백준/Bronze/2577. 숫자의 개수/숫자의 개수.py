def main():
    A = int(input())
    B = int(input())
    C = int(input())
    result = A * B * C
    arr = [0 for i in range(10)]
    length = len(str(result))
    for i in range(length - 1, -1, -1):
        arr[result // 10 ** i] += 1
        result = result % 10 ** i
    for i in arr:
        print(i)
main()