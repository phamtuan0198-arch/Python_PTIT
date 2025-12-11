import sys
a = sys.stdin.read().strip().split()
b = []
for ch in a:
    b.append(int(ch) % 42)
print(len(set(b)))