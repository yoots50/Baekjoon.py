def isPalindrome(string):
    return string == string[::-1]

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True

def main():
    N = int(input())
    n = N
    while not (isPalindrome(str(n)) and isPrime(n)):
        n += 1
    print(n)
    
main()