def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        res = "NO"
    else:
        if (x2-x1)%(v2-v1) == 0:
            res = "YES"
        else:
            res = "NO"
    return res

print(kangaroo(0,3,4,2))    # harusnya YES
print(kangaroo(21,6,47,3))  # harusnya NO