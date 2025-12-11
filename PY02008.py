import math

def ngto(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

a , b = map(int, input().split())
i = 1
Ngto = []
while len(Ngto) < a:
    if(ngto(i)):
        Ngto.append(i)
    i += 1
print(b , end=" ")
for x in(Ngto):
    print(b + x, end= " ")
    b = b + x












