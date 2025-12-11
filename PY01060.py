for _ in range(int(input())):
    n = input()
    sum , res = 0 , 1
    for i in range(len(n)):
        if i % 2:
            sum += int(n[i])
        else:
            if n[i] != '0':
                res *= int(n[i])
    print(f"{res} {sum}")