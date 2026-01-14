import queue


def bfs(graph, start, visited):
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = u
                q.put(v)


def main():
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    visited = [-1] * (N + 1)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    bfs(graph, 1, visited)
    for i in range(2, N + 1):
        print(visited[i])


if __name__ == "__main__":
    main()
