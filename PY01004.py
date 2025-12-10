import math

def nt(a):
    if  a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    cnt = 0
    n = int(input())
    for i in range(1 , n):
        if math.gcd(i , n) == 1: cnt += 1

    if nt(cnt): print("YES")
    else: print("NO")