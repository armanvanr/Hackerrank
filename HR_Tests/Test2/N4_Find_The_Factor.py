def pthFactor(n, p):  # 5/13
    res = []
    for num in range(1, n // 2):
        if n % num == 0:
            res.append(num)
            res.append(n // num)
    res.sort()
    print(res)
    if p > len(res):
        return 0
    else:
        return res[p - 1]


print(pthFactor(20, 10))
# print(pthFactor(1048576,12))


def pthFactor2(n, p):  # 7/13
    res = []
    for num in range(1, n + 1):
        if n % num == 0:
            res.append(num)
    res.sort()
    if p > len(res):
        return 0
    else:
        return res[p - 1]


# print(pthFactor2(1,1)) # output:1
# print(pthFactor2(1048576,12))


def pthFactor3(n, p):  # 7/13 tested
    res = []
    lim = (n // 2) + 2
    for num in range(1, lim):
        if n % num == 0:
            res += [num, n // num]
    res = sorted(set(res))
    print(res)
    if p > len(res):
        return 0
    else:
        return res[p - 1]


# print(pthFactor3(1,1)) # output:1
# print(pthFactor3(1048576,12)) # 2048
# print(pthFactor3(20,10))


def pthFactor4(n, p):  # SOLVED 13/13
    res = []
    lim = int(n**0.5) + 1
    for num in range(1, lim):
        if n % num == 0:
            res += [num, n / num]
    res = sorted(set(res))
    if p > len(res):
        return 0
    else:
        return res[p - 1]


# TAHAPAN PENYELESAIAN:
# 1. cari faktornya, masukkan ke dalam sebuah list
# 2. unique dan sort
# 3. return faktor di posisi p, kalo dia ga ada (p is out of range) return 0

# Misal, B = A/X
# suatu bilangan X disebut faktor bilangan A, jika A mod X tidak bersisa (A%X==0)
# hasil baginya (B) juga merupakan faktor bilangan A
# sehingga X dan B merupakan faktor A
# suatu bilangan minimal punya 2 faktor, yaitu 1 dan bilangan itu sendiri, lebih dikenal dengan bilangan prima
# misal 2,3,5,7,11,dst
# kecuali 1, faktornya cuma ada satu
# konteksnya spesifik bilangan asli ya, bukan bulat, desimal, dll

# ALGORITMA
# cek faktor dari n
# loop dari 1 sampai suatu batas
# batasnya akar n, misal n=36, loop dari 1 sampai 6
# jika n mod num == 0, masukkan n dan hasil baginya ke dalam list baru
# bikin unique list lalu sort
# return faktor di posisi p
