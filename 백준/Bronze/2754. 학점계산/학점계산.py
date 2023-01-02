def main():
    grade = input()
    base = 69 - ord(grade[0])
    if (len(grade) == 2):
        if (grade[1] == '+'):
            print("%0.1f" % (base + 0.3))
        elif (grade[1] == '-'):
            print("%0.1f" % (base - 0.3))
        else:
            print("%0.1f" % base)
    else:
        print(0.0)
main()
