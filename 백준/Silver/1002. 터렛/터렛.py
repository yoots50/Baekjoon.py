import math

def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if r1 < r2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            r1, r2 = r2, r1
        if x1 == x2 and y1 == y2:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        elif dist + r2 <= r1:
            if dist + r2 == r1:
                print(1)
            else:
                print(0)
        else:
            if dist == r1 + r2:
                print(1)
            elif dist < r1 + r2:
                print(2)
            else:
                print(0)

if __name__ == "__main__":
    main()