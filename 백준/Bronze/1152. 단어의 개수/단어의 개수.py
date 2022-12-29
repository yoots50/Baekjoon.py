def main():
    string = input().strip()
    if string == '':
        print(0)
        return 0
    cnt = 1
    while True:
        if string.find(' ') + 1:
            string = string[string.find(' ') + 1:]
            cnt += 1
        else:
            print(cnt)
            return 0
main()