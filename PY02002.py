for _ in range(int(input())):
    a , b = map(int , input().split())
    fibo = [0] * (b + 2)
    fibo[0] = 0 
    fibo[1] = 1
    for i in range(2 , b + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    for i in range(a , b + 1):
        print(fibo[i], end= " ")
    print()