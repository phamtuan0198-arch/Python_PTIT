b = []
a , k , n = map(int , input().split())
for i in range(k , n + 1, k):
    if i - a > 0:
        b.append(i - a)
if len(b) == 0: print(-1)
else:
    print(*b)