from itertools import combinations

n , k = map(int , input().split())
a = list(map(int, input().split()))
a = sorted(set(a))

for ch in combinations(a , k):
    print(*ch)