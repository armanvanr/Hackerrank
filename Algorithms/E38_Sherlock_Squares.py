import math
def squares1(a, b):
    count = 0
    for num in range(a, b + 1):
        z = (num**0.5) % 2
        if z == 0 or z == 1:
            count += 1
    return count
# print(squares1(3, 9))
# algoritma pertama
# menghitung akar dari square, jika di belakang koma tidak ada angka maka dia square
# misal, a=3, b=10, looping dari 3 sampai 10, ada square 4 dan 9
# akar 3 = 1.73 => 1.73/2 sisa 1 atau 0? False, bukan square
# akar 4 = 2.00 => 2.00/2 sisa 1 atau 0? True, square
# tidak efisien untuk bilangan besar misal a dan b jutaan, karena di-loop satu satu, bertambah satu

def squares(a,b):
    count=0
    a = (math.ceil(a**0.5))**2
    b = (math.floor(b**0.5))**2
    d = int((a**0.5)*2 -1)
    # print("a","num","b","d")
    num = a
    while a<=num<=b:
        count+=1
        d+=2
        num+=d
        # print(a,num,"  ",b,d)
    # print("count", count)
    return count
squares(2,64)

# algoritma kedua, terinspirasi dari barisan aritmatika tingkat dua
# lihat tabel square di excel
# kita akan melooping bilangan square nya aja
# dimulai dari square terdekat dari a dan square terdekat b (yang ada di rentang inklusif a sampai b)
# setiap kali looping, counter bertambah satu (increment 1)

# misal, berapa banyak square dari 3 hingga 10?
# kita akan looping dimulai dari square terdekat 3 yaitu 4
# dan berakhir di square terdekat 10

# cara menemukan square berikutnya:
# jarak antara satu square ke square berikutnya selalu bertambah
# tapi pertambahan jaraknya selalu sama, yaitu 2
# square berikutnya = square sekarang + d
# d nya increment 2
# "nilai awal d" yaitu akar dari "square awal" dikali 2, dikurang 1
