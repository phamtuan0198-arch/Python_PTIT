import math

def coso10(n):
    a = 0
    for i in range(0 , len(n)):
        a += int(n[-i - 1]) * (2 ** i)
    return a

def doicoso(n , coso):
    a = coso10(n)
    b = ''
    while(a != 0):
        du = a % coso
        if (du > 9):
            b = chr(ord('A') + du - 10) + b
        else:
            b = str(du) + b
        a //= coso
    return b

for _ in range(int(input())):
    coso = int(input())
    n = input()
    if coso == 2:
        print(n)
    else:
        print(doicoso(n , coso))
