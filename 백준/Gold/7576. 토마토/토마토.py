import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start):
    q = deque(start)
    maxDate = 0
    while q:
        v = q.popleft()
        x = v[0]
        y = v[1]
        prevDate = graph[x][y]
        if prevDate > maxDate:
            maxDate = prevDate
        if x > 0 and graph[x - 1][y] == 0:
            graph[x - 1][y] = prevDate + 1
            q.append((x - 1, y))
        if x < len(graph) - 1 and graph[x + 1][y] == 0:
            graph[x + 1][y] = prevDate + 1
            q.append((x + 1, y))
        if y > 0 and graph[x][y - 1] == 0:
            graph[x][y - 1] = prevDate + 1
            q.append((x, y - 1))
        if y < len(graph[0]) - 1 and graph[x][y + 1] == 0:
            graph[x][y + 1] = prevDate + 1
            q.append((x, y + 1))
    return maxDate - 1


def main():
    M, N = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i] = list(map(int, input().split()))
    start = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                start.append((i, j))

    maxDate = bfs(graph, start)

    isAllRipe = True
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)
                isAllRipe = False
                break
        if not isAllRipe:
            break

    if isAllRipe:
        print(maxDate)


if __name__ == "__main__":
    main()
