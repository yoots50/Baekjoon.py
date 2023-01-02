def main():
    string = input()
    alphaTable = [-1 for i in range(26)]
    for i in range(len(string)):
        if (alphaTable[ord(string[i]) - 97] == -1):
            alphaTable[ord(string[i]) - 97] = i
    for i in alphaTable:
        print(i, end = " ")
main()