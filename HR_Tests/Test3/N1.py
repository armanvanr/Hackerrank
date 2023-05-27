def isPower(arr):
    res = []
    for num in arr:
        base2 = bin(num)[2:]
        count1 = base2.count("1")
        if count1 == 1:
            res.append(1)
        elif count1 !=1:
            res.append(0)
    return res


# print(isPower([137, 1999998, 1048577, 33554432, 15]))  ##output: [0,0,0,1,0]
print(isPower([16, 24, 56, 48, 0, 1, 100, 99])) # output: [1, 0, 0, 0, 0, 1, 0, 0]
lst = [2, 3, 4, 8, 12, 16, 33554432]
# for num in lst:
#     # print(num,"mod2",num%2)
#     # print(num,"mod4",num%4)
#     a = bin(num)[2:]
#     x = a.count("1")
#     print(num, "bin:", a, "num of 1:", x)
