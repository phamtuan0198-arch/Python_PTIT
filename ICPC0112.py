import math

def checknt(a):
    if a < 2:
        return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(5 , n - 5):
        if (checknt(i) and checknt(i + 2) and checknt(i + 6)) or (checknt(i) and checknt(i + 4) and checknt(i + 6)):
            cnt += 1
    print(cnt)