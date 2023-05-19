def getMaximumMEX(arr):  # 1/15
    n = len(arr)
    res = []
    for i in range(n):
        if arr[i] != i and i not in arr:
            res.append(i)
    return max(res)


def gmm(arr):  # 2/15
    n = len(arr)
    res = [(max(arr) + 1)]
    for i in range(n):
        if arr[i] != i and i not in arr:
            res.append(i)
    return max(res)


def get_max_mex(arr):  # ?/15
    print(f"initial: {arr}")
    arr.sort()
    for i, num in enumerate(arr):
        for x in range(0, num):
            if x not in arr:
                arr[i] = x
                # break
    print(f"reduced: {arr}")
    mex = max(arr) + 1
    print(f"mex    :  {mex}\n")


z = [2,2,2,2,2,2]
a = [0, 0]  # output: 1
b = [1, 2, 2]  # output: 3
c = [2, 0, 0]  # output: 2
d = [3, 2, 3]  # output: 3
e = [1, 2]  # output: 2
f = [0, 1, 2, 3, 5]  # output: 5

for x in (z, a, b, c, d, e, f):
    get_max_mex(x)

# Algoritma
# Urutkan array, sort ascending
# Loop 1: baca setiap bilangan (num)
# Loop 2: cek nilai x yang memenuhi dua syarat
#       apakah ada x yang kurang dari num? 0 <= x <= num-1
#       apakah x tersebut tidak ada di dalam array?
# kalo ada nilai x yang memenuhi,
# perbarui num dengan x tersebut, dan keluar dari loop 2 (break)
# Setelah loop 1 selesai, maka MEX nya adalah nilai maximum array+1
