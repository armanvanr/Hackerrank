def birthday(s, d, m):
    count = 0
    i = 0
    while i < len(s):
        z=s[i : i + m]
        if sum(z) == d: #potong array, jumlahkan elemennya, bandingkan dengan d
            count += 1
        i += 1
    return count


print(birthday([2, 2, 1, 3, 2], 4, 2))
# ketika i = 4, slicing s[4:6] alias slicing elemen index 4 sampai 5 tetap jalan, bukan "index out of range"
# padahal listnya cuma punya elemen index 0-4

# print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
# print(birthday([4], 4, 1))
# print(birthday([3, 2, 1, 3, 1], 9, 4))

def birthday_choco(s,d,m):
    count=0
    for i in range(len(s)-(m-1)):
        if sum(s[i:i+m])==d: count+=1
    return count