import math

def ngto(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
freq = {}
for ch in(a):
    if(ngto(ch)):
        freq[ch] = freq.get(ch , 0) + 1
for ch in(freq):
    print(f"{ch} {freq[ch]}")