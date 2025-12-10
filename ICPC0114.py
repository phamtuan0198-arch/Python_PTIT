import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    n = int(input())
    if not nt(n):
        print("No")
        continue
    x = str(n)
    if not nt(int(x[::-1])):
        print("No")
        continue
    sum = 0
    ok = True
    while n > 0:
        if not nt(n % 10):
            print("No")
            ok = False
            break
        sum += n % 10
        n //= 10
    if ok:
        if nt(sum): print("Yes")
        else: print("No")