for _ in range(int(input())):
    a , b = map(int , input().split())
    n = list(map(int , input().split()))
    for i in range(b, a):
        print(n[i], end= " ")
    for i in range(0, b):
        print(n[i], end= " ")
    print()
