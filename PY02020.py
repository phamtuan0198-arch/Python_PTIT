n = int(input())
a = list(map(float, input().split()))
a.sort()
min_a = a[0]
max_a = a[n - 1]
b = []
sum_b = 0.0
for ch in(a):
    if(ch != min_a and ch != max_a):
        b.append(ch)
        sum_b += ch
res = sum_b / len(b)
print(f"{res:.2f}")