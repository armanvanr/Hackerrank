def changeAds(base10):  # 8/8
    base2 = bin(base10)
    num = base2[2:]
    str1 = ""
    for i in range(len(num)):
        if num[i] == "0":
            str1 += "1"
        else:
            str1 += "0"
    return int("0b" + str1, base=2)


print(changeAds(30))
print(changeAds(50))


def change_ads(base10):  # 8/8
    base2 = bin(base10)[2:]
    str1 = ""
    for i in range(len(base2)):
        if base2[i] == "0":
            str1 += "1"
        else:
            str1 += "0"
    return int("0b" + str1, base=2)


print(change_ads(30))
print(change_ads(50))
