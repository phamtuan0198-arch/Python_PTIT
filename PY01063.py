for _ in range(int(input())):
    n = input()
    m = input()
    cnt, i  = 0 , 0
    while i < len(n) - len(m) + 1:
        if n[i : i + len(m)] == m:
            cnt += 1
            i += len(m)
        else: i += 1
    print(cnt)