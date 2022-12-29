func = lambda A, B: ">" if A > B else "<" if A < B else "=="
A, B = map(int , input().split())
print(func(A, B))