from collections import deque


def D(A):
    return (A * 2) % 10000


def S(A):
    if A == 0:
        return 9999
    return A - 1


def L(A):
    return (A // 1000) + (A % 1000) * 10


def R(A):
    return (A - (A % 10)) // 10 + (A % 10) * 1000


def bfs(A, B):
    q = deque()
    q.append(A)
    while q:
        now = q.popleft()
        if now == B:
            return visited[now]
        if visited[D(now)] == "" and D(now) != A:
            visited[D(now)] = visited[now] + "D"
            q.append(D(now))
        if visited[S(now)] == "" and S(now) != A:
            visited[S(now)] = visited[now] + "S"
            q.append(S(now))
        if visited[L(now)] == "" and L(now) != A:
            visited[L(now)] = visited[now] + "L"
            q.append(L(now))
        if visited[R(now)] == "" and R(now) != A:
            visited[R(now)] = visited[now] + "R"
            q.append(R(now))


def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        global visited
        visited = [""] * 10000
        print(bfs(A, B))


if __name__ == "__main__":
    main()
