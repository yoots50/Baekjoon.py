def checkCondition(i, j, N, graph, visited):
    if (not (0 <= i and i <= N - 1)):
        return 0
    if (not (0 <= j and j <= N - 1)):
        return 0
    if (graph[i][j] == '0'):
        return 0
    if (visited[i][j] == 1):
        return 0
    return 1

def load(cnt, visited, queue, i, j):
    visited[i][j] = 1
    cnt += 1
    queue.append([i, j])
    return cnt

def BFS(graph, N):

    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = []
    cnt = 0
    cntArr = []
    
    for fi in range(N):
        for fj in range(N):
            if visited[fi][fj] == 0:
                visited[fi][fj] = 1
                if graph[fi][fj] == '1':
                    queue.append([fi, fj])
                    cnt += 1
                    while (queue):
                        i, j = queue.pop(0)
                        if (checkCondition(i + 1, j, N, graph, visited)):
                            cnt = load(cnt, visited, queue, i + 1, j)
                        if (checkCondition(i - 1, j, N, graph, visited)):
                            cnt = load(cnt, visited, queue, i - 1, j)
                        if (checkCondition(i, j + 1, N, graph, visited)):
                            cnt = load(cnt, visited, queue, i, j + 1)
                        if (checkCondition(i, j - 1, N, graph, visited)):
                            cnt = load(cnt, visited, queue, i, j - 1)
                    cntArr.append(cnt)
                    cnt = 0

    return cntArr
                    

def main():

    N = int(input())
    graph = []

    for _ in range(N):
        graph.append(input())

    cntArr = BFS(graph, N)

    print(len(cntArr))

    cntArr.sort()

    for c in cntArr:
        print(c)
        
main()