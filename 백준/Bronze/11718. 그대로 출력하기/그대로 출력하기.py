def main():
    while True:
        try:
            print(input())
        except EOFError:
            return 0
main()