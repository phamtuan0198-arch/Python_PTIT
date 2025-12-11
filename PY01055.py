for _ in range(int(input())):
    n = input()
    ok = True
    if len(n) % 2:
        if n[0] == n[1]: ok = False
        for i in range(2 , len(n) ,2):
            if n[i] != n[0]:
                ok = False
                break
        if ok: print("YES")
        else: print("NO")
    else: print("NO")