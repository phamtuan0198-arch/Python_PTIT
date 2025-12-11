for _ in range(int(input())):
    n = input()
    ok = True
    for i in range(len(n)):
        if n[i] not in '012': 
            ok = False
            break
    if ok: print("YES")
    else: print("NO")