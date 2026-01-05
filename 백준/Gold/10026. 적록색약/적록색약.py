import sys
from collections import deque

input = sys.stdin.readline


def bfs1(graph, startx, starty, visited):
    visited[startx][starty] = True
    q = deque()
    q.append([startx, starty])
    s = graph[startx][starty]
    while q:
        u = q.popleft()
        x = u[0]
        y = u[1]
        if x > 0 and visited[x - 1][y] == False and graph[x - 1][y] == s:
            visited[x - 1][y] = True
            q.append([x - 1, y])
        if x < len(graph) - 1 and visited[x + 1][y] == False and graph[x + 1][y] == s:
            visited[x + 1][y] = True
            q.append([x + 1, y])
        if y > 0 and visited[x][y - 1] == False and graph[x][y - 1] == s:
            visited[x][y - 1] = True
            q.append([x, y - 1])
        if y < len(graph) - 1 and visited[x][y + 1] == False and graph[x][y + 1] == s:
            visited[x][y + 1] = True
            q.append([x, y + 1])


def bfs2(graph, startx, starty, visited):
    visited[startx][starty] = True
    q = deque()
    q.append([startx, starty])
    while q:
        u = q.popleft()
        x = u[0]
        y = u[1]
        if x > 0 and visited[x - 1][y] == False and graph[x - 1][y] in ["R", "G"]:
            visited[x - 1][y] = True
            q.appendleft([x - 1, y])
        if (
            x < len(graph) - 1
            and visited[x + 1][y] == False
            and graph[x + 1][y] in ["R", "G"]
        ):
            visited[x + 1][y] = True
            q.appendleft([x + 1, y])
        if y > 0 and visited[x][y - 1] == False and graph[x][y - 1] in ["R", "G"]:
            visited[x][y - 1] = True
            q.appendleft([x, y - 1])
        if (
            y < len(graph) - 1
            and visited[x][y + 1] == False
            and graph[x][y + 1] in ["R", "G"]
        ):
            visited[x][y + 1] = True
            q.appendleft([x, y + 1])


def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i] = input()

    visited1 = [[False for _ in range(N)] for _ in range(N)]
    visited2 = [[False for _ in range(N)] for _ in range(N)]
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if visited1[i][j] == False:
                bfs1(graph, i, j, visited1)
                cnt1 += 1
            if visited2[i][j] == False:
                if graph[i][j] == "B":
                    bfs1(graph, i, j, visited2)
                    cnt2 += 1
                else:
                    bfs2(graph, i, j, visited2)
                    cnt2 += 1
    print(cnt1, cnt2)


if __name__ == "__main__":
    main()
