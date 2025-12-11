for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in(a):
        freq[x] = freq.get(x , 0) + 1
    max_freq = max(freq.values())
    if(max_freq > n / 2):
        b = set(a)
        for ch in(b):
            if(freq[ch] == max_freq):
                print(ch)
                break
    else:
        print("NO")
    
        
    












