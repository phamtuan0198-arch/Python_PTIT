n = int(input())

def Try(s , cnt, i):
    if len(s) == i:
        if len(set(s)) < 3: return
        if cnt['A'] > cnt['B'] or cnt['B'] > cnt['C']: return
        print(s)
        return
    for ch in 'ABC':
        cnt[ch] += 1
        Try(s + ch , cnt , i)
        cnt[ch] -= 1

for i in range(3 , n + 1):
    cnt = {'A' : 0, 'B' : 0, 'C' : 0}
    Try("" , cnt , i)