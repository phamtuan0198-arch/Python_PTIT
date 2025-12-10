for _ in range(int(input())):
    ok = True
    n = input()
    for i in range(0 , len(n) - 1):
        if n[i] > n[i + 1]:
            ok = False
            break
    if ok: print("YES")
    else: print("NO")