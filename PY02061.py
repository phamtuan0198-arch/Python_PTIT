dx = [-1 , -1 , -1 , 0 , 0 , 0, 1 , 1, 1]
dy = [-1 , 0 , 1 , -1 , 0 , 1 , -1, 0 , 1]
for _ in range(int(input())):
    a = []
    x , y = map(int, input().split())
    for _ in range(x):
        b = list(map(int, input().split()))
        a.append(b)
    b = []
    for _ in range(3):
        c = list(map(int, input().split()))
        b.append(c)
    res = 0
    for i in range(1, x-1):
        for j in range(1, y-1):
            val = 0
            for u in range(3):
                for v in range(3):
                    val += a[i + u - 1][j + v - 1] * b[u][v]
            res += val
    print(res)