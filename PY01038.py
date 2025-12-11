for _ in range(int(input())):
    n = input()
    if int(n) % 7 == 0: print(n)
    else:
        cnt = 0
        while cnt < 1000:
            
            if (int(n) + int(n[::-1])) % 7 == 0:
                print(int(n) + int(n[::-1]))
                break
            n = str(int(n) + int(n[::-1]))
            cnt += 1
        if cnt == 1000: print(-1)