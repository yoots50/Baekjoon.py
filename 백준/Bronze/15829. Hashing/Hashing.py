L = int(input())
string = input()

Sum = 0

for i in range(L):
    Sum += (ord(string[i]) - ord('a') + 1) * (31 ** i)

print(Sum % 1234567891)
