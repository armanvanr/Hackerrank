def multiple(m, n):
    return sum(range(m,n,m))

def multiple_3_and_5(n):
    mul3 = multiple(3,n)
    mul5 = multiple(5,n)
    mul15 = multiple(15,n)
    return mul3+mul5-mul15

print(multiple_3_and_5(10))
