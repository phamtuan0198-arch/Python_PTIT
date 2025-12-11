n = int(input())
a = list(map(int, input().split()))
ok = True
a.sort()
for i in range(0 , len(a) - 1):
    if(a[i + 1] - a[i] != 1):
        print(a[i] + 1)
        ok = False
        break
if ok:
    print(a[-1] + 1)


    
        
    












