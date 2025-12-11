for _ in range(int(input())):
    n = int(input())
    ok, sum = True , 0
    while n > 0:
        sum += n % 10
        if n > 9 and abs((n // 10) % 10 - n % 10) != 2:
            ok = False
            break
        n //= 10
    if sum % 10: ok = False
    if ok: print("YES")
    else: print("NO")