def main():
    N = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)
    av = sum(arr) / N
    answer = av / M * 100
    print(answer)
main()
