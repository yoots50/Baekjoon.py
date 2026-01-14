def dfs(p, visited, status):
    if len(status) == M:
        for i in range(M):
            print(status[i], end="")
            if i != M - 1:
                print(" ", end="")
        print()

    nowvisit = []
    for i in range(0, N):
        if p[i] not in nowvisit and visited[i] == False:
            nowvisit.append(p[i])
            visited[i] = True
            status.append(p[i])
            dfs(p, visited, status)
            status.pop()
            visited[i] = False


def main():
    global N, M
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    visited = [False] * N
    dfs(p, visited, [])


if __name__ == "__main__":
    main()