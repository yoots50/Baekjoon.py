def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0 for i in range(N)]
    rank = 0
    for i in range(1, 1001):
        for j in range(N):
            if A[j] == i:
                ans[j] = rank
                rank += 1
    for i in range(len(ans)):
        print(ans[i], end="")
        if not i == len(ans) - 1:
            print(" ", end="")


if __name__ == "__main__":
    main()
