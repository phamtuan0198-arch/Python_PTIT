for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pair = []
    for ch in(a):
        x = ch
        res = 0
        while(x > 0):
            res += x % 10
            x //= 10
        pair.append((ch , res))
    pair.sort(key= lambda x : (x[1], x[0]))
    for ch in(pair):
        print(ch[0], end=" ")
    print()