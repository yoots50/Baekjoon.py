def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)
    ans = sum(map(lambda a, b: a * b, A, B))
    print(ans)

if __name__ == "__main__":
    main()