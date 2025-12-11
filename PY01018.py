p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    x = input().split()
    if int(x[0]) == 0: break
    k , s = x[0] , x[1]
    res = ""
    for ch in s:
        idx = p.index(ch)
        res = p[(idx + int(k)) % 28] + res
    print(res)