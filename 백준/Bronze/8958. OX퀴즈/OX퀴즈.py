def main():
    T = int(input())
    for i in range(T):
        string = input()
        cnt = 0
        amount = 0
        for s in string:
            if (s == 'O'):
                cnt += 1
            else:
                amount += cnt * (cnt + 1) // 2
                cnt = 0
        amount += cnt * (cnt + 1) // 2
        print(amount)
        cnt = 0

main()