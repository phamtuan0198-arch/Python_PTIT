for _ in range(int(input())):
    n = input()
    ok = True
    sum , res = 0 , 1
    for i in range(len(n)):
        if i % 2:
            if n[i] != '0':
                ok = False
                res *= int(n[i])
        else: sum += int(n[i])
    if ok: print(f"{sum} {0}")
    else: print(f"{sum} {res}")