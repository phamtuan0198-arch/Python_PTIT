import sys

x = sys.stdin.read().strip().split()
t = x[0]
i = 1
for _ in range(int(t)):
    q , p = x[i], x[i + 1]
    if q < p:
        q , p = p , q
    x1 , x2 = x[i + 2], x[i + 3]
    i += 4
    print(f'{int(x1.replace(q , p)) + int(x2.replace(q , p))} {int(x1.replace(p , q)) + int(x2.replace(p , q))}') 