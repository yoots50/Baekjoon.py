import sys

def main():

    N = int(input())
    arr = [0 for i in range(10001)]

    for _ in range(N):
        arr[int(sys.stdin.readline())] += 1

    for i in range(10001):
        for _ in range(arr[i]):
            sys.stdout.write("%d\n" % i);
            

main()