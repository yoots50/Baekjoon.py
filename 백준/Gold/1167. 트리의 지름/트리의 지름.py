import sys

sys.setrecursionlimit(10**6)


def dfs(graph, start, visited):
    visited[start] = True
    childCnt = 0
    tmp = []
    for v in graph[start]:
        if not visited[v[0]]:
            visited[v[0]] = True
            childCnt += 1
            tmp.append(dfs(graph, v[0], visited) + v[1])
    if childCnt == 0:
        return 0
    tmp.sort(reverse=True)
    if childCnt > 1:
        ans.append(tmp[0] + tmp[1])
    return tmp[0]


def main():
    V = int(input())
    graph = [[] for _ in range(V + 1)]
    for i in range(V):
        tmp = list(map(int, input().split()))
        p = tmp[0]
        tmp = tmp[1:-1]
        for j in range(len(tmp) // 2):
            graph[p].append([tmp[j * 2], tmp[j * 2 + 1]])
    global ans
    ans = []
    ans.append(dfs(graph, 1, [False for _ in range(V + 1)]))
    print(max(ans))


if __name__ == "__main__":
    main()
