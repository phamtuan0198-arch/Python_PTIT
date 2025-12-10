import math

def nt(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    a = []
    n = int(input())
    for i in range(13 , n):
        x = str(i)
        if x == x[::-1]: continue
        if nt(int(x)) and nt(int(x[::-1])) and int(x[::-1]) < n:
            if i not in a:
                a.append(i)
                a.append(int(x[::-1]))
    print(*a)
