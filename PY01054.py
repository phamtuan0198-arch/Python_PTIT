for _ in range(int(input())):
    n = input()
    res = 1
    for ch in n:
        if ch != '0':
            res *= int(ch)
    print(res)