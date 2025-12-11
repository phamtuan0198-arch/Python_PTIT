while True:
    a = list(map(int, input().split()))
    cnt = 0
    if(len(set(a)) == 1 and a[0] == 0):
        break
    else:
        while(len(set(a)) != 1):
            x = a[0]
            for i in range(0 , 3):
                a[i] = abs(a[i] - a[i + 1])
            a[3] = abs(a[3] - x)
            cnt += 1
        print(cnt)