def saveThePrisoner(n, m, s):
    r = n-(s-1)
    num = (m-r)%n
    if num == 0:
        return n
    else:
        return num

# a,b,c=208526924, 756265725, 150817879 #expected output:72975907
# a,b,c=10,30,3
# a,b,c = 9999,9999,1
# print(saveThePrisoner(4,6,2))
# print(saveThePrisoner(a,b,c))

# r : range, rentang antara penerima permen pertama (s) hingga kursi ke n
# misal n=10, m=24, s=3, => r=8 (ada 8 orang pertama yang menerima permen)
#     v v v v v v v  v
# 1 2 3 4 5 6 7 8 9 10

# (m-r)mod n: sisa permen pembagian pertama tadi sejumlah (m-r) dibagikan ke n
# kalo sisa akhir (num) nol, maka penerima terakhir adalah n
# kalo tidak, penerima terakhir adalah kursi ke-(num)

# # algoritma:
# kalau start nya dari 1:
# permen = permen awal = m
# kursi terakhir = permen mod n
# permen = 12
# start = 1
# orang = 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2

# kalo start nya bukan dari 1:
# permen = permen sisa = permen awal - (banyak orang - start -1)
# kursi terakhir = permen mod n
# permen = 12
# start = 3
# orang = 5
# - - 3 4 5 x
# 1 2 3 4 5
# 1 2 3 4

# jika kursi terakhir = 0, return banyak orang (n)
# jika tidak, return kursi terakhir