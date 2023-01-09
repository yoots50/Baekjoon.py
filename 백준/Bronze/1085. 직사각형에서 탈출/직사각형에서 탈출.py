def main():
    x, y, w, h = map(int, input().split())
    disup = h - y
    disdown = y
    disright = w - x
    disleft = x
    print(min(disup, disdown, disright, disleft))

main()