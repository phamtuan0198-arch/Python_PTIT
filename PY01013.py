import math
def nt(a):
    if a < 2: return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    n , m = map(int , input().split())
    GCD, sum = math.gcd(n , m), 0
    while GCD > 0:
        sum += GCD % 10
        GCD //= 10
    if nt(sum): print("YES")
    else: print("NO")
