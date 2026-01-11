def main():
    global A, B
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    Ai = [[] for i in range(101)]
    Bi = [[] for i in range(101)]
    for i in range(N):
        Ai[A[i]].append(i)
    for i in range(M):
        Bi[B[i]].append(i)
    ans = []
    Aidx = -1
    Bidx = -1
    for i in range(100, 0, -1):
        Ai[i] = [a for a in Ai[i] if a > Aidx]
        Bi[i] = [b for b in Bi[i] if b > Bidx]
        minlen = min(len(Ai[i]), len(Bi[i]))
        for j in range(minlen):
            ans.append(i)
            Aidx = Ai[i][j]
            Bidx = Bi[i][j]
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i], end="")
        if i != len(ans) - 1:
            print(" ", end="")


if __name__ == "__main__":
    main()
