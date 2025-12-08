import math

for _ in range(int(input())):
    Max = 0
    n = input()
    a = ""
    for ch in n:
        if ch >= '0' and ch <= '9':
            a += ch
            Max = max(Max , int(a))
        else:
            a = ""
    print(Max)

