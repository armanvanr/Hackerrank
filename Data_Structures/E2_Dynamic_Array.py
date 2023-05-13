def dynamicArray(n, queries):
    arr=[[] for _ in range(n)]
    lastAns = 0
    res=[]
    for q in queries:
        x=q[1]
        y=q[2]
        idx = (x^lastAns)%n
        if q[0] == 1:
            arr[idx].append(y)
        else:
            lastAns=arr[idx][y%len(arr[idx])]
            res.append(lastAns)
    return res
print(dynamicArray(2, [1, 0, 5]))