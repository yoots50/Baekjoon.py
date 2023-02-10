def main():
    lst = input().split()
    for i in range(8):
        if (lst[i] != '1' and lst[i] != '0'):
            print("F")
            return 0
    print("S")

main()