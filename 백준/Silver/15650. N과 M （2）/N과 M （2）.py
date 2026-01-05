def dfs(arr, start, now):
    if len(now) == M:
        for i in range(len(now)):
            if i < len(arr) - 1:
                print(now[i], end=" ")
            else:
                print(now[i])
        print()
        return
    if start < N:
        for i in range(start + 1, N):
            now.append(arr[i])
            dfs(arr, i, now)
            now.pop()


def main():
    global N, M
    N, M = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    for i in range(N):
        dfs(arr, i, [i + 1])


if __name__ == "__main__":
    main()
