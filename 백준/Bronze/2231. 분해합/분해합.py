def main():
    N = int(input())
    for i in range(1, N):
        if (i + sum(map(int, list(str(i)))) == N):
            print(i)
            return 0
    print(0)
    
main()