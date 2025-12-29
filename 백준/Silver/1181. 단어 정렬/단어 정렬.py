def main():
    N = int(input())
    words = set()
    for i in range(N):
        words.add(input())
    words = list(words)
    words.sort(key=lambda word: (len(word), word))
    for word in words:
        print(word)


if __name__ == "__main__":
    main()