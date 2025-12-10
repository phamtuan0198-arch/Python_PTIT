n = input()
cnt = 0
for ch in n:
    if ch >= 'a' and ch <= 'z': cnt += 1
if cnt >= len(n) // 2: print(n.lower())
else: print(n.upper())