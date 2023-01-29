scores = []

memo = [[0 for _ in range(302)] for _ in range(302)]

def func(now, prev):
    if (now == 1):
        return scores[0]
    if (now == 2):
        if (prev - now == 1):
            return scores[1]
        return scores[1] + scores[0]
    if (memo[now][prev] != 0):
        return memo[now][prev]
    if (prev - now == 1):
        memo[now][prev] = scores[now - 1] + func(now - 2, now)
        return memo[now][prev]
    memo[now][prev] = scores[now - 1] + max(func(now - 2, now), func(now - 1, now))
    return memo[now][prev]

def main():
    N = int(input())
    
    for _ in range(N):
        scores.append(int(input()))

    print(func(N, N))

main()