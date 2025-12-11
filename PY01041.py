for _ in range(int(input())):
    n = input()
    ok = True 
    if len(n) < 3: print("NO")
    else:
        idx = 0
        for i in range(1 , len(n)):
            if idx == i - 1 and n[i] > n[i - 1]:
                idx = i
                continue
            if idx and n[i] >= n[i - 1]:
                ok = False
                break
        if idx == 0 or idx == len(n) - 1: ok = False
        if ok: print("YES")
        else: print("NO")
