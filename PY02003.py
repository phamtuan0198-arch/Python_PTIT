import bisect

limit = 10 ** 18
hamming = [1]
i2 , i3 ,i5 = 0 ,0 , 0
while True:
    next2 = hamming[i2] * 2
    next3 = hamming[i3] * 3
    next5 = hamming[i5] * 5
    next_hamming = min(next2 , next3, next5)
    if next_hamming > limit: break
    hamming.append(next_hamming)
    if next_hamming == next2: i2 += 1
    if next_hamming == next3: i3 += 1
    if next_hamming == next5: i5 += 1

for _ in range(int(input())):
    n = int(input())
    idx = bisect.bisect_left(hamming , n)
    if idx < len(hamming) and hamming[idx] == n:
        print(idx + 1) 
    else: print("Not in sequence")