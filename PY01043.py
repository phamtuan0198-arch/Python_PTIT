res = []
def sodep(a , n):
    if a != "":
        if int(a) == 0 or int(a + a[::-1]) >= n: return
        res.append(int(a + a[::-1]))
    for i in range(0 , 10 , 2):
        sodep(a + str(i) , n)
    return

for _ in range(int(input())):
    res.clear()
    n = int(input())
    sodep("" , n)
    res.sort()
    print(*res)