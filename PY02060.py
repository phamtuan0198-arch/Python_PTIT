from sys import stdin
from math import isqrt

mod = 10**9 + 7
data = stdin.read().strip().split()
T = int(data[0])
pairs = []
idx = 1
b_max = 0
for _ in range(T):
    a = int(data[idx]); b = int(data[idx+1])
    idx += 2
    pairs.append((a,b))
    b_max = max(b_max, b)

prime = []
isprime = [True]*(b_max+1)
isprime[0] = isprime[1] = False
for i in range(2, isqrt(b_max)+1):
    if isprime[i]:
        for j in range(i*i, b_max+1, i):
            isprime[j] = False
prime = [i for i in range(2, b_max+1) if isprime[i]]

def count(x, n):
    c = 0
    while n:
        n //= x
        c += n
    return c

for a, b in pairs:
    ans = 1
    half = b // 2
    for p in prime:
        if p > half: break
        val = (count(p, b) - count(p, a-1)) * 2 + 1
        ans = (ans * val) % mod
    m = 0
    for p in prime:
        if p > half and p <= b:
            m += 1

    ans = ans * pow(3, m, mod) % mod
    print(ans)