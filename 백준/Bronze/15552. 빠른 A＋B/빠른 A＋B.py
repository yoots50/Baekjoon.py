import sys
def main():
    T = int(input())
    for i in range(0, T):
        A, B = map(int, sys.stdin.readline().split())
        sys.stdout.write("%d\n" % (A + B))
main()