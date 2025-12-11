import math
def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if not a % i: return False
    return True

for _ in range(int(input())):
    n = input()
    ok, sum = True, 0
    for i in range(len(n)):
        if i % 2 and not int(n[i]) % 2: ok = False
        if not i % 2 and int(n[i]) % 2: ok = False
        sum += int(n[i])
    if not nt(sum): ok = False
    if ok: print("YES")
    else: print("NO")