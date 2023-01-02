def main():
    string = input()
    for i in range(0, len(string)):
        if string[i].isupper():
            print(string[i].lower(), end = '')
        else:
            print(string[i].upper(), end = '')
main()