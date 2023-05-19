def countPairs(projectCosts, target): #7/10
    n=len(projectCosts)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if abs(projectCosts[i]-projectCosts[j])==target:
                count+=1
    return count

print(countPairs([1,3,5],2))

def countPairs(projectCosts, target): #7/10
    n=len(projectCosts)
    f=[1 for i in range(n) for j in range(i+1,n) if abs(projectCosts[i]-projectCosts[j])==target]

    return len(f)