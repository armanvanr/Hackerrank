def gmm(arr): # 1/15 passed
    mex=[]
    for x in range(len(arr)):
        if x not in arr:
            mex.append(x)
    return max(mex)

def getMaximumMEX(arr):
    mex=[]
    for x in range(max(arr)):
        if x not in arr:
            idx=arr.index(max(arr))
            arr[idx]=x
    return mex, arr

# print(getMaximumMEX([1,0,2,3,5])) #output 4
# print(getMaximumMEX([3,1,2,2])) # output 3
# print(getMaximumMEX([2,0,0])) # output 2

def gm(arr):
    arr.sort()
    uni=sorted(list(set(arr)))
    mex=[]
    n=len(arr)
    temp = []
    for x in range(n+1):
        if x not in arr:
            temp.append(x)
    mex.append(min(temp))
    for num in uni:
        if arr.count(num)>1:
            idx = arr.index(num)
            arr[idx] = mex[0]
    print(arr, uni, mex)
    temp = []
    for x in range(n+1):
        if x not in arr:
            temp.append(x)
    mex.append(min(temp))
    print(arr, uni, mex)
    # return mex
print(gm([3,1,2,2]))