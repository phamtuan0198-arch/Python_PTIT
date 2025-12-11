import math

for _ in range(int(input())):
    n = input()
    if math.gcd(int(n) , int(n[::-1])) == 1: print("YES")
    else: print("NO")