import math

def ngto(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

a , b = map(int, input().split())
n = []
for i in range(0 , a):
    row = list(map(int , input().split()))
    for j in range(0 , b):
        if(ngto(row[j])):
            row[j] = 1
        else:
            row[j] = 0
    n.append(row)
for ch in(n):
    print(*ch)
