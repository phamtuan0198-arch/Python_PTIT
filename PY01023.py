import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    n = int(input())
    if n == 1: print(1)
    else: 
        print("1 * ", end="")
        x = 0
        a = []
        for j in range(2 , int(math.sqrt(n)) + 1):
            if n % j == 0 and nt(j):
                while n % j == 0:
                    x += 1
                    n //= j
                a.append(f'{j}^{x}')
                x = 0
        if n != 1: a.append(f'{n}^1')
        print(' * '.join(a))