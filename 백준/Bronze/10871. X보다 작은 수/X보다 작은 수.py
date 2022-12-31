import sys
def main():
    N, X = map(int, input().split())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(0, N):
        if (arr[i] < X):
            sys.stdout.write("%d " % arr[i])
main()