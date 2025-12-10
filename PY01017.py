for _ in range(int(input())):
    n = input()
    x = 1
    for i in range (0 , len(n) - 1):
        if n[i] != n[i + 1]:
            print(f"{x}{n[i]}", end="")
            x = 1
        else:
            x += 1
    print(f"{x}{n[-1]}")