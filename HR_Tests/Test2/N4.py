def pthFactor(n, p): #5/13
    res = []
    for num in range(1, n//2):
        if n%num == 0:
            res.append(num)
            res.append(n//num)
    res.sort()
    print(res)
    if p> len(res):
        return 0
    else:
        return res[p-1]
    
# print(pthFactor(20,10))
# print(pthFactor(1048576,12))

def pthFactor2(n, p): #7/13
    res = []
    for num in range(1, n+1):
        if n%num == 0:
            res.append(num)
    res.sort()
    if p> len(res):
        return 0
    else:
        return res[p-1]

# print(pthFactor2(1,1)) # output:1
# print(pthFactor2(1048576,12))

def pthFactor3(n, p): # ?/13
    res = []
    lim=(n//2)+2
    for num in range(1, lim):
        if n%num == 0:
            res+=res+[num, n//num]
    res=(sorted(set(res)))
    print(res)
    if p> len(res):
        return 0
    else:
        return res[p-1]
    
# print(pthFactor3(1,1)) # output:1
print(pthFactor3(1048576,12)) # 2048
# print(pthFactor3(20,10))