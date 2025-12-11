import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    n = input()
    if not nt(len(n)): print("NO")
    else:
        cnt1 , cnt2 = 0 , 0
        for ch in n:
            if nt(int(ch)): cnt1 += 1
            else: cnt2 += 1
        if cnt1 > cnt2: print("YES")
        else: print("NO")