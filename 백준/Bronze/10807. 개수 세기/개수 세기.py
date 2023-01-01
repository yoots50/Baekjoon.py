import sys
def main():
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    v = int(input())
    cnt = 0
    for i in arr:
        if (i == v):
            cnt += 1
    print(cnt)
main()