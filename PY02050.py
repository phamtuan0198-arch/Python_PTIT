for _ in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    st , res = [] , []
    st.append(0)
    res.append(1)
    for i in range(1 , n):
        while st and a[i] >= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            res.append(i + 1)
        else:
            res.append(i - st[-1])
        st.append(i)
    print(*res)