def main():
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    words.sort()
    ans = N
    for i in range(len(words) - 1):
        if words[i] == words[i + 1][: len(words[i])]:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()