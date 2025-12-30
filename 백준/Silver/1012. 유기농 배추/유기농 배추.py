def bfs(graph, startx, starty, visited):
    visited[startx][starty] = 1
    q = [(startx, starty)]
    while q:
        p = q.pop(0)
        x, y = p[0], p[1]
        if x != 0 and graph[x - 1][y] and visited[x - 1][y] != 1:
            visited[x - 1][y] = 1
            q.append((x - 1, y))
        if x != len(graph) - 1 and graph[x + 1][y] and visited[x + 1][y] != 1:
            visited[x + 1][y] = 1
            q.append((x + 1, y))
        if y != 0 and graph[x][y - 1] and visited[x][y - 1] != 1:
            visited[x][y - 1] = 1
            q.append((x, y - 1))
        if y != len(graph[0]) - 1 and graph[x][y + 1] and visited[x][y + 1] != 1:
            visited[x][y + 1] = 1
            q.append((x, y + 1))


def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().split())
            graph[y][x] = 1
        visited = [[0 for _ in range(M)] for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    cnt += 1
                    bfs(graph, i, j, visited)
        print(cnt)


if __name__ == "__main__":
    main()