n = int(input())
st, x = [], 0
while n > 0:
    st.append(n % 10)
    n //= 10
    x += 1
    if x == 3 and n > 0:
        st.append(",")
        x = 0
while st:
    print(st.pop(), end="")
print()