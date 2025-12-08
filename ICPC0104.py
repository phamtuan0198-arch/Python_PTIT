import math

for _ in range(int(input())):
    Min = 10 ** 19
    n = input()
    a = ""
    for ch in n:
        if ch >= '0' and ch <= '9':
            a += ch
        else:
            if len(a) != 0:
                Min = min(Min , int(a))
                a = ""
    print(Min)

