import math

n = int(input())
a = []
b = list(map(int , input().split()))
for ch in b:
    if len(a) == 0:
        a.append(ch)
    else:
        if (a[-1] + ch) % 2 == 0:
            a.pop()
        else:
            a.append(ch)
print(len(a))