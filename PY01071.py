def check(a):
    for ch in(a):
        if not(ch >= 'a' and ch <= 'z' or ch == "." or ch == '_'):
            return False  
    return True

n = input()
n = n.lower()
if(n[-3:] == '.py' and check(n)):
    print("yes")
else:
    print("no")











