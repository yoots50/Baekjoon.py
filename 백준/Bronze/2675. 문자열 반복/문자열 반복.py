def main():
    T = int(input())
    for i in range(T):
        R, string = input().split()
        R = int(R)
        for i in string:
            print(i * R, end = '')
        print("")
        
main()