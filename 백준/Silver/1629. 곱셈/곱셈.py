def power(x, y, mod):
    if (y == 0):
        return 1
    xmod = x % mod
    if (y == 1):
        return xmod
    if (y % 2 == 1):
        return xmod * power(xmod * xmod % mod, y // 2, mod)
    return power(xmod * xmod % mod, y // 2, mod)

def main():
    A, B, C = map(int, input().split())
    print(power(A % C, B, C) % C)

if __name__ == "__main__":
    main()