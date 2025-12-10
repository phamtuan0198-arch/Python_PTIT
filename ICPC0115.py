def gt(n):
    res = 1
    for i in range(2 , n + 1):
        res *= i
    return res

for _ in range(int(input())):
    n = int(input())
    x, sum = n, 0
    while x > 0:
        sum += gt(x % 10)
        x //= 10
    if sum == n:
        print("Yes")
    else:
        print("No")