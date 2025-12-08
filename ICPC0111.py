import math

def ngto(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    a , b = map(int , input().split())
    n = list(map(int , input().split()))
    for i in range(b, len(n)):
        print(n[i], end= " ")
    for i in range(0, b):
        print(n[i], end= " ")
    print()
    


