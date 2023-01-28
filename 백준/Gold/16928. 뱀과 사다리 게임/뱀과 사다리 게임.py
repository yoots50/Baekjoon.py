def BFS(ladderStart, ladderEnd, snakeStart, snakeEnd):
    visited = [0 for _ in range(102)]
    memo = [0 for _ in range(102)]
    start = 1
    memo[start] = 0
    queue = []
    queue.append(start)
    visited[start] = 1

    ans = []

    while (queue):
        
        start = queue.pop(0)

        for i in range(start + 1, start + 7):

            if (i == 100):
                ans.append(memo[start] + 1)
                break
            
            if (i in ladderStart):
                end = ladderEnd[ladderStart.index(i)]
                if (visited[end] == 0):
                    queue.append(end)
                    visited[end] = 1
                    memo[end] = memo[start] + 1
                
            elif (i in snakeStart):
                end = snakeEnd[snakeStart.index(i)]
                if (visited[end] == 0):
                    queue.append(end)
                    visited[end] = 1
                    memo[end] = memo[start] + 1

            else:
                end = i
                if (visited[end] == 0):
                    queue.append(end)
                    visited[end] = 1
                    memo[end] = memo[start] + 1
    
    return min(ans)

def main():

    N, M = map(int, input().split())
    ladderStart = []
    ladderEnd = []
    snakeStart = []
    snakeEnd = []

    for _ in range(N):
        i, j = map(int, input().split())
        ladderStart.append(i)
        ladderEnd.append(j)

    for _ in range(M):
        i, j = map(int, input().split())
        snakeStart.append(i)
        snakeEnd.append(j)

    print(BFS(ladderStart, ladderEnd, snakeStart, snakeEnd))
    
main()
