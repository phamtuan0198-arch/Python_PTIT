from itertools import permutations

n = input()
for ch in permutations(n):
    print("".join(ch))