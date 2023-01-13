import math
def main():
    A, B, V = map(int, input().split())
    print(math.ceil((V - A) / (A - B) + 1))
    
main()