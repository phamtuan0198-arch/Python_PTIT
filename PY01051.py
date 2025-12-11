for _ in range(int(input())):
    n = int(input())
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    s = str(sum)
    if len(s) > 1 and s == s[::-1]: print("YES")
    else: print("NO")