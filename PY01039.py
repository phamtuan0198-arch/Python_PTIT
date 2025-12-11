for _ in range(int(input())):
    n = input()
    ok = True
    if len(set(n)) != 2: print("NO")
    else:
        for i in range(len(n) - 2):
            if n[i] != n[i + 2]:
                ok = False
                break
        if ok: print("YES")
        else: print("NO")
    