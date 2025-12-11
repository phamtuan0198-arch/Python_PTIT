for _ in range(int(input())):
    freq = {}
    a = []
    for _ in range(int(input())):
        x = int(input())
        a.append(x)
        freq[x] = freq.get(x , 0) + 1
    max_freq = max(freq.values())
    a = set(a)
    a = sorted(a)
    for ch in(a):
        if(freq[ch] == max_freq):
            print(ch)
            break













