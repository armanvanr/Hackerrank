def circularArrayRotation(a, k, queries):
    for _ in range(k):
        a.insert(0, a[-1])
        a.pop(-1)
    res = [a[i] for i in queries]
    return res

print(circularArrayRotation([1,2,3],2,[0,1,2]))