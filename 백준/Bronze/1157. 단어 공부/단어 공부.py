def main():
    string = input()
    alpha = [0 for i in range(26)]
    for i in string:
        alpha[ord(i.lower()) - 97] += 1
    almax = max(alpha)
    cnt = 0
    for i in alpha:
        if i == almax:
            cnt += 1
            idx = alpha.index(i)
        if cnt == 2:
            print("?")
            return 0
    print(chr(idx + 65))
main()