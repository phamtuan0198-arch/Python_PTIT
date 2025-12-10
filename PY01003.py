for _ in range(int(input())):
    n = input()
    
    a = ''
    du  = 0
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) + du > 4:
            du = 1
        else:
            du = 0 
        a = '0' + a
    if int(n[0]) + du > 9:
        a = '10' + a
    else:
        a = str(int(n[0]) + du) + a
    print(a)