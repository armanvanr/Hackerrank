def isPossible(a, b, c, d): #6/10
    x = (c - a) % b
    i = (c - a) // b

    y = (d - b) % a
    j = (d - b) // a
    if x == 0:
        a = c
        if (d - b) % a == 0:
            return "Yes"
        else:
            return "No"
    if y == 0:
        b = d
        if (c - a) % b == 0:
            return "Yes"
        else:
            return "No"

def ip(a, b, c, d): #8/10
    x = (c - a) % b
    if x == 0:
        a = a + b
        y = (d - b) % a
        if y == 0:
            return "Yes"
        else:
            return "No"
    return "No"

def ip2(a,b,c,d): #7/10
    x = (c - a) % b
    y = (d - b) % a
    if x == 0:
        a = a + b
        if (d - b) % a == 0:
            return "Yes"
        else:
            return "No"
    if y == 0:
        b = a + b
        if (c - a) % b == 0:
            return "Yes"
        else:
            return "No"

# 1,4,5,9 YES
# 1,2,3,6 NO
# print(isPossible(1, 2, 3, 6))  # NO
print(ip2(2, 2, 2, 1000))  # YES
print(ip2(1, 4, 62, 45))  # YES
