
for _ in  range(int(input())):
    n = int(input())
    a = sorted(map(int , input().split()))
    cnt = 0
    for i in range(n):
        l , r = i + 1, n - 1
        while(l < r):
            sum = a[i] + a[l] + a[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                cnt += 1
                l += 1
    print(cnt)