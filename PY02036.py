import math
def ngto(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(0 , n - 1):
    for j in range(i + 1, n):
        if(math.gcd(a[i] , a[j]) == 1):
            print(f"{a[i]} {a[j]}")
