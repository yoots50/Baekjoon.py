from collections import deque


def bfs(A, B):
    queue = deque()
    queue.append((A, 0))
    while queue:
        now = queue.popleft()
        if now[0] == B:
            return now[1] + 1
        if now[0] < B:
            queue.append((now[0] * 2, now[1] + 1))
            queue.append((now[0] * 10 + 1, now[1] + 1))
    return -1


def main():
    A, B = map(int, input().split())
    print(bfs(A, B))


if __name__ == "__main__":
    main()
