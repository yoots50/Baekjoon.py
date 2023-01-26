def BFS(graph, i, j, N, M):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = []
    visited[i][j] = 1
    queue.append([i, j])
    memo = [[0 for _ in range(M)] for _ in range(N)]
    memo[i][j] = 1
    while (queue):
        x, y = queue.pop(0)
        if (x == M - 1 and y == N - 1):
            return memo[N - 1][M - 1]
        if (x != M - 1 and visited[y][x + 1] == 0 and graph[y][x + 1] == '1'):
            visited[y][x + 1] = 1
            memo[y][x + 1] = memo[y][x] + 1
            queue.append([x + 1, y])
        if (y != N - 1 and visited[y + 1][x] == 0 and graph[y + 1][x] == '1'):
            visited[y + 1][x] = 1
            memo[y + 1][x] = memo[y][x] + 1
            queue.append([x, y + 1])
        if (x != 0 and visited[y][x - 1] == 0 and graph[y][x - 1] == '1'):
            visited[y][x - 1] = 1
            memo[y][x - 1] = memo[y][x] + 1
            queue.append([x - 1, y])
        if (y != 0 and visited[y - 1][x] == 0 and graph[y - 1][x] == '1'):
            visited[y - 1][x] = 1
            memo[y - 1][x] = memo[y][x] + 1
            queue.append([x, y - 1])
            
        

def main():

    N, M = map(int, input().split())
    graph = [0 for _ in range(N)]
    for i in range(N):
        graph[i] = input()

    print(BFS(graph, 0, 0, N, M))
            

main()