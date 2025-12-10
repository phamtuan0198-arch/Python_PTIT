for _ in range(int(input())):
    n = input()
    if n[0:2] != n[-2::]:
        print ("NO")
    else:
        print("YES")