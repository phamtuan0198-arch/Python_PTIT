import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if not a % i: return False
    return True

for _ in range(int(input())):
    n = input()
    ok = True
    for i in range(len(n)):
        if nt(i) and not nt(int(n[i])):
            ok = False
            break
        if not nt(i) and nt(int(n[i])):
            ok = False
            break
    if ok: print("YES")
    else: print("NO")