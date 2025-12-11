n = int(input())
res_up = 0
res_dow = 0
for i in range(0 , n):
    row = list(map(int , input().split()))
    for j in range(0 , n):
        if(j + i < n - 1):
            res_up += row[j]
        if(j + i > n - 1):
            res_dow += row[j]
k = int(input())
if abs(res_up - res_dow) <= k:
    print("YES")
else:
    print("NO")
print(abs(res_up - res_dow))



    
        
    












