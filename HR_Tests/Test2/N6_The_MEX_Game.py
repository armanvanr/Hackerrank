import numpy


def getMaximumMEX(arr):  # 1/15
    n = len(arr)
    res = []
    for i in range(n):
        if arr[i] != i and i not in arr:
            res.append(i)
    return max(res)


def getMaximumMEX2(arr):  # 2/15
    n = len(arr)
    res = [(max(arr) + 1)]
    for i in range(n):
        if arr[i] != i and i not in arr:
            res.append(i)
    return max(res)


def gmm1(arr):  # 7/15
    print(f"initial: {arr}")
    arr.sort()
    for i, num in enumerate(arr):
        for x in range(0, num):
            if x not in arr:
                arr[i] = x
                break
    print(f"reduced: {arr}")
    mex = max(arr) + 1
    print(f"mex    :  {mex}\n")


def gmm2(arr):  # 7/15
    # print(f"initial: {arr}")
    arr.sort()
    z = 0
    for i, num in enumerate(arr):
        for x in range(
            z, num
        ):  # batas bawah loop bertambah 1 untuk mengurangi jumlah iterasi
            if x not in arr:
                arr[i] = x
                z = x + 1
                break
    # print(f"reduced: {arr}")
    mex = max(arr) + 1
    # print(f"mex    :  {mex}\n")
    return mex


# single loop only
def gmm3(arr):
    uniq = sorted(list(set(arr)))
    f = [arr.count(num) for num in uniq]
    prev = -1
    for i, num in enumerate(uniq):
        np = num - prev
        if np == 1:
            prev = num
        else:
            d = f[i] - np
            if d >= 0:
                prev = num
            else:
                prev += f[i] % np
    mex = prev + 1
    return mex


# optimasi nested if dari getmaxmex3
def gmm4(arr):
    uniq = sorted(list(set(arr)))
    f = [arr.count(num) for num in uniq]
    prev = -1
    for i, num in enumerate(uniq):
        np = num - prev
        d = f[i] - np
        if d >= 0:
            prev = num
        else:
            prev += f[i] % np
    mex = prev + 1
    return mex


def gmm5(arr):  # SOLVED 15/15
    a = numpy.array(arr)
    nums, f = numpy.unique(a, return_counts=True)
    prev = -1
    for i, num in numpy.ndenumerate(nums):
        np = num - prev
        d = f[i] - np
        if d >= 0:
            prev = num
        else:
            prev += f[i] % np
    mex = prev + 1
    return mex


z = [2, 2, 2, 2, 2, 2]  # output: 3
a = [0, 0]  # output: 1
b = [1, 2, 2]  # output: 3
c = [2, 0, 0]  # output: 2
d = [3, 2, 3]  # output: 3
e = [1, 2]  # output: 2
f = [0, 1, 2, 3, 5]  # output: 5
y = [10000] * 50  # output: 50

for x in (a, b, c, d, e, f, y):
    print(gmm5(x))

# Tahapan penyelesaian
# Yang diminta soal, kita tentukan MEX setiap modifikasi array, append MEX itu ke suatu list (list_MEX)
# Setelah array berkali-kali dimodifikasi dan dapet bentuk final, dari list itu kita ambil maksimum dari list_MEX

# Langkah optimal
# 1. modifikasi array awal jadi array final
# 2. tentukan maximum dari MEX nya (pasti maximum MEX nya adalah nilai max dari array final +1)

# ALGORITMA gmm1 dan gmm2
# Urutkan array, sort ascending
# Loop 1: baca setiap bilangan (num)
# Loop 2: cek nilai x yang memenuhi dua syarat
#       apakah ada x yang kurang dari num? 0 <= x <= num-1
#       apakah x tersebut tidak ada di dalam array?
# kalo ada nilai x yang memenuhi,
# perbarui num dengan x tersebut, dan keluar dari loop 2 (break)
# Setelah loop 1 selesai, maka MEX nya adalah nilai maximum array+1

# ALGORITMA gmm3
# Buat array unique dan sorted ascending
# Hitung frekuensi dari masing-masing unique item
# Loop array unique tsb sampe item terakhir

# Tentukan apakah kita harus mereduksi num itu atau tidak,
# Kalo iya, reduksi seluruhnya atau sebagian saja?
# Hitung selisih antara item tersebut (num) dengan bilangan sebelumnya (prev)
#   kalo selisih nya 1
#       update prev sekarang adalah num
#       misal, arr [2,3,4,10]
#       dari 2->3, 3->4

#   kalo selisihnya lebih dari 1
#       misal, arr [2,3,4,10]
#       kalo 10 nya ada satu doang, 10 jadi 5
#           dari 4->10
#           prev sekarang 5
#       kalo 10 nya ada banyak,
#           prev nya tergantung frekuensi dari si 10
#           (prev baru) adalah (prev lama) ditambah sisa dari (frekuensi_num) dibagi (np)
#           prev = prev + (f[i] mod np)

# prev awal bernilai -1 karena unique pertama bisa jadi 0
# return prev+1 sebagai nilai maksimum dari MEX

# ALGORITMA gmm4
# sama seperti gmm3 tapi nested conditional disederhanakan

# ALGORITMA gmm5
# sama seperti gmm4 tapi menggunakan numpy untuk mendapat performa yang lebih cepat
# syarat pake "tipe data array" adalah tipe datanya harus seragam
