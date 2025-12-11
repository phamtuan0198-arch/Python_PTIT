import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if not a % i: return False
    return True

for _ in range(int(input())):
    n = int(input())
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    if nt(sum): print("YES")
    else: print("NO")