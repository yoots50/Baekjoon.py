import sys

N = int(sys.stdin.readline().strip())
_sum = 0
mid = []
freq = [0 for _ in range(8001)]
_min = 4000
_max = -4000

for _ in range(N):
    n = int(sys.stdin.readline().strip())
        
    _sum += n

    mid.append(n)
    
    freq[n + 4000] += 1

    if (_min > n):
        _min = n
        
    if (_max < n):
        _max = n
    


tmp = 0
idx = 0
tf = True
for i in range(8001):
    if (tmp == freq[i] and tf):
        idx = i
        tf = False
    if (tmp < freq[i]):
        idx = i
        tmp = freq[i]
        tf = True
    

print(int(round(_sum / N, 0)))
print(sorted(mid)[N // 2])
print(idx - 4000)
print(_max - _min)