def main():
    
    N = int(input())
    i = 0
    amount = 1
    while True:
        if (N <= amount):
            print(i + 1)
            return 0
        else:
            i += 1
            amount += 6 * i

main()