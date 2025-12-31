from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = [0 for _ in range(len(graph))]
    visited[start] = 1
    cnt = 0
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if visited[u] == 0:
                visited[u] = 1
                queue.append(u)
                cnt += 1
    return cnt


def main():
    N = int(input())
    V = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(V):
        v = list(map(int, input().split()))
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    print(bfs(graph, 1))


if __name__ == "__main__":
    main()