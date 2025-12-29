def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            visited[node] = True
            dfs(graph, node, visited)


def bfs(graph, start, visited):
    visited[start] = True
    q = [start]
    while q:
        p = q.pop(0)
        print(p, end=" ")
        for node in graph[p]:
            if not visited[node]:
                visited[node] = True
                q.append(node)


def main():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        tmp = list(map(int, input().split()))
        graph[tmp[0]].append(tmp[1])
        graph[tmp[1]].append(tmp[0])
    for i in range(N + 1):
        graph[i].sort()
    visited = [False] * len(graph)
    dfs(graph, V, visited)
    print()
    visited = [False] * len(graph)
    bfs(graph, V, visited)


if __name__ == "__main__":
    main()