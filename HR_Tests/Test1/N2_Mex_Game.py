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

print(getMaximumMEX([1,0,2,3,5])) #output 4
# print(getMaximumMEX([3,1,2,2])) # output 3
# print(getMaximumMEX([2,0,0])) # output 2
