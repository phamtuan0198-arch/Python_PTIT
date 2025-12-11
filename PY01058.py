import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if not a % i: return False
    return True

for _ in range(int(input())):
    n = input()
    if nt(int(n[-4:])): print("YES")
    else: print("NO")