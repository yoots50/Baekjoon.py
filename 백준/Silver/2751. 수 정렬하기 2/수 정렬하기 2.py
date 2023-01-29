import sys

def main():
    N = int(sys.stdin.readline())

    arr = [0 for _ in range(2000001)]

    for _ in range(N):
        
        arr[int(sys.stdin.readline()) + 1000000] += 1

    for idx in range(2000001):
        if (arr[idx] > 0):
            sys.stdout.write("%d\n" % (idx - 1000000))
main()