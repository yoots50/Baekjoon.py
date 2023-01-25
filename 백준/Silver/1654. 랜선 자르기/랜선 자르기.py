def main():
    
    K, N = map(int, input().split())

    lan_line = []

    for _ in range(K):
        lan_line.append(int(input()))

    start = 0
    end = max(lan_line) + 1
    
    while end - start > 1:
        cnt = 0
        mid = (end + start) // 2
        for line in lan_line:
            cnt += line // mid
        if cnt >= N:
            start = mid
        else:
            end = mid

    print(start)
            

main()