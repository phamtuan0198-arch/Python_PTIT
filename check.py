
a = []
cnt = 0

def Try(pre, sum, ind, n):
    global cnt #dung bien cuc bo cnt
    if sum > 0: return
    if ind == 2: 
        cnt += 1
        return
    for i in range(pre, n):
        Try(i + 1, sum + a[i], ind , n)
    return

for t in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    cnt = 0
    Try(0, 0, 0, n)
    print(cnt)