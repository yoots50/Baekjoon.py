def main():
    H, M = map(int, input().split())
    if (M < 45):
        if (H == 0):
            print(23, 15 + M)
        else:
            print(H - 1, 15 + M)
    else:
        print(H, M - 45)

main()