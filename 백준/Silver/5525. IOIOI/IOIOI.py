def main():
    N = int(input())
    M = int(input())
    S = input()
    status = "EMPTY"
    cnt = 0
    ans = 0
    for i in range(M):
        if status == "EMPTY" and S[i] == "I":
            status = "I"
        elif status == "I" and S[i] == "O":
            status = "IO"
        elif status == "IO" and S[i] == "I":
            cnt += 1
            status = "I"
        else:
            if cnt - N + 1 > 0:
                ans += cnt - N + 1
            cnt = 0
            if status == "IO":
                status = "EMPTY"

    if cnt - N + 1 > 0:
        ans += cnt - N + 1

    print(ans)


if __name__ == "__main__":
    main()
