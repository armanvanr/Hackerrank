def permutationEquation(p):
    n=len(p)
    z= []
    y = [0 for _ in range(n)] # list zeros, isinya nol sebanyak n [0,0,0,0,0]
    for i in range(n):
        x=i+1
        temp = p.index(x)
        a = p.index(temp+1)
        y[i] = a+1
        z.append(a+1)
    return y, z
print(permutationEquation([5,2,1,3,4]))