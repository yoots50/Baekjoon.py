import sys

def main():
    
    M, N = map(int, input().split())
    
    if M <= 1:
        M = 2
        
    arr = [i for i in range(0, N + 1)]
    
    for i in range(2, N + 1):
       if (arr[i] != 0):
           j = 1
           while i + j * arr[i] < N + 1:
               arr[i + j * arr[i]] = 0
               j += 1
    
    for i in arr:
        if i != 0 and i != 1 and M <= i:
            sys.stdout.write("%d\n" % i)

main()