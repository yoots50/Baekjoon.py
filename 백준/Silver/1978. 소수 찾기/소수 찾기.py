def main():
    input()
    input_arr = list(map(int, input().split()))
    prime_filter = [i for i in range(2, max(input_arr) + 1)]
    for idx in range(0, len(prime_filter)):
        now = prime_filter[idx]
        if (now != 0):
            i = 1
            while (i * now + idx < len(prime_filter)):
                prime_filter[i * now + idx] = 0
                i += 1
    cnt = 0
    for i in input_arr:
        if i > 1:
            if prime_filter[i - 2] != 0:
                cnt += 1

    print(cnt)


            

main()