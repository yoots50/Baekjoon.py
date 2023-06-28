def mul(n, m):
    ret = 1
    for i in range(n, m + 1):
        ret *= i
    return ret

def comb(N, M):
    num = mul(N - M + 1, N)
    den = mul(1, M)

    return num // den

def main():

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        print(comb(M, N))
    
if __name__ == "__main__":
    main()