import numpy as np
def arrayManipulation(n, queries):
    #cara2
    arr = np.zeros((n,), dtype=int)
    que = np.array(queries)
    for q in que:
        a,b,k=q[0],q[1],q[2]
        for i in range(a,b+1):
            a,b,k=q[0],q[1],q[2]
            arr[i-1]+=k
    return np.amax(arr)


    # #cara1
    # arr = [0 for _ in range(n)]
    # for q in queries:
    #     a,b,k=q[0],q[1],q[2]
    #     for i in range(a,b+1):
    #         arr[i-1]+=k
    # return max(arr)
    

print(arrayManipulation(5, [[1, 2, 100],[2, 5, 100],[3, 4, 100]]))