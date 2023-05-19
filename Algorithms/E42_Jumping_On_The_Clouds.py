def jumpingOnClouds(c):
    n = len(c)
    i, jumps = 0, 0
    while i < n - 1:
        if (i + 2 <= n - 1) and c[i + 2] == 0:
            i += 2
        elif c[i + 1] == 0:
            i += 1
        jumps += 1
    return jumps


a = [0, 0, 1, 0, 0, 1, 0]
b = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(a))

# # Algoritma
# loop array cloud menggunakan while supaya jarak lompatnya nya bisa diatur, increment 2 atau 1
# langkah minimum diperoleh jika dia jarak stepnya 2 setiap mendarat di awan
# jadi cek dulu bisa gak dia lompat ke awan berikutnya dengan jarak step 2,
# kalo ga bisa ambil jarak step 1

# untuk kondisi jarak step 2, perlu ada kondisi tambahan: jika lompatan berikutnya masih ada cloud maka loncat,
# kalo ga bisa, ambil jarak step 1