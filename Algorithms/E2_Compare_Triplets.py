def compareTriplets(a, b):

    i = 0
    a_score = 0
    b_score = 0
    while i < len(a):
        if b[i] > a[i]:
            b_score += 1
        elif a[i] > b[i]:
            a_score += 1
        i += 1
    return [a_score, b_score]

x = [5, 6, 7]
y = [3, 6, 10] 
print(compareTriplets(x,y))
