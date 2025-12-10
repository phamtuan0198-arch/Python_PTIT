for _ in range(int(input())):
    n = input()
    ok = True
    for ch in n:
        if ch != '4' and ch != '7':
            ok = False
            break
    if ok : print("YES")
    else: print("NO")